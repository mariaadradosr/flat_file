emp_tw = pd.read_excel(path+'/'+files[0],sheet_name = 'Teleweb Empresas', header=6)
# Definción de qué filas hay que quitar, aquéllas que no tengan formato fecha
rows_to_drop = [e for e in range(len(emp_tw)) if type(emp_tw.iloc[e,0]) != pd._libs.tslibs.timestamps.Timestamp ]
emp_tw = emp_tw.drop(rows_to_drop)
emp_tw = emp_tw[emp_tw.columns[emp_tw_columns_to_keep]].fillna(0)
emp_tw.rename(columns = emp_tw_cols, inplace=True)
emp_tw.iloc[:,1:] = emp_tw.iloc[:,1:].astype('float64')
emp_tw['vtas_movil_web'] = emp_tw['vtas_movil_tw_web']-emp_tw['vtas_movil_tw']
emp_tw['vtas_fijo_web'] = emp_tw['vtas_fijo_tw_web']-emp_tw['vtas_fijo_tw']
emp_tw.drop(columns = ['vtas_movil_tw_web','vtas_fijo_tw_web'],inplace = True)