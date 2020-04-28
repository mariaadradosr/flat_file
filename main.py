import pandas as pd
import os
import static
import functions

input_path = './input/'
output_path = './output/'

files = os.listdir(input_path)



def main():
    print('Creating 1414_Total: 1414 Residencial + 1414 Empresas')
    res_1414 = functions.llam_1414(path = input_path, files = files, sheet = '1414 Residencial', header = 5, cols = static.res_1414_cols_to_keep, col_names = static.res_1414_cols)
    emp_1414 = functions.llam_1414(path = input_path, files = files, sheet = '1414 Empresas', header = 6, cols = static.emp_1414_cols_to_keep, col_names = static.emp_1414_cols)
    tot_1414 = pd.concat([res_1414,emp_1414],axis = 0,join ='outer',ignore_index = True, sort= False).fillna(0)
    tot_1414.to_csv(f'{output_path}tot_1414.csv', decimal=",",encoding='CP1252',index=False)
    print('1414 Total csv exported ok')
    print('\nCreating Tw_Total: Teleweb Residencial + Teleweb Empresas')
    res_tw = functions.teleweb(path=input_path, files=files, sheet='Teleweb Residencial', header=6, cols = static.res_tw_cols_to_keep, col_names=static.res_tw_cols)
    emp_tw = functions.teleweb(path=input_path, files=files, sheet='Teleweb Empresas', header=6, cols = static.emp_tw_cols_to_keep, col_names=static.res_tw_cols)
    tot_tw = pd.concat([res_tw,emp_tw],axis = 0,join ='outer',ignore_index = True, sort= False).fillna(0)
    tot_tw.to_csv(f'{output_path}tot_tw.csv', decimal=",",encoding='CP1252',index=False)
    print('Teleweb Total csv exported ok')
if __name__ == "__main__":
    main()