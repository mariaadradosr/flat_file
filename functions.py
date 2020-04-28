import pandas as pd

def llam_1414(path, files, sheet, header, cols, col_names):
    df = pd.read_excel(path+files,sheet_name = sheet, header=header)
    # Definción de qué filas hay que quitar, aquéllas que no tengan formato fecha
    rows_to_drop = [e for e in range(len(df)) if type(df.iloc[e,0]) != pd.Timestamp ]
    df = df.drop(rows_to_drop)
    df = df[df.columns[cols]].fillna(0)
    df.rename(columns = col_names, inplace=True)
    df.iloc[:,1:] = df.iloc[:,1:].astype('float64')
    df['sheet'] = sheet
    return df


def teleweb(path, files, sheet, header, cols, col_names):
    df = pd.read_excel(path+files,sheet_name = sheet, header=header)
    # Definción de qué filas hay que quitar, aquéllas que no tengan formato fecha
    rows_to_drop = [e for e in range(len(df)) if type(df.iloc[e,0]) != pd.Timestamp ]
    df = df.drop(rows_to_drop)
    df = df[df.columns[cols]].fillna(0)
    df.rename(columns = col_names, inplace=True)
    df.iloc[:,1:] = df.iloc[:,1:].astype('float64')
    df['vtas_movil_web'] = df['vtas_movil_tw_web']-df['vtas_movil_tw']
    df['vtas_fijo_web'] = df['vtas_fijo_tw_web']-df['vtas_fijo_tw']
    df.drop(columns = ['vtas_movil_tw_web','vtas_fijo_tw_web'],inplace = True)
    df['sheet'] = sheet 
    return df