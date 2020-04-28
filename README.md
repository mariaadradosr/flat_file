## Descripción 
Programa escrito en python para aplanar el fichero de llamadas Orange

## Modulos python:
- pandas
- xlrd (mac)

## Archivos:
- `static.py` contiene los siguientes elementos:
    - 4 listas de las columnas que necesitamos por pestaña
    - 3 diccionarios con el mapeo del nombre de las columnas
- `functions.py` contiene dos funciones que transforman el contenido de las pesatañas en dataframes depurados
- `main.py` contiene el código que ejecutará el programa para obtener:
    - `tot_1414.csv` Archivo con las columnas necesarias de la parte del 1414 que agrupa tanto la pestaña de residencial como la de empresas
    - `tot_tw.csv` Archivo con las columnas necesarias de la parte de teleweb que agrupa tanto la pestaña de residencial como la de empresas

## Modo de empleo:
Para su uso simplemente habrá que crear en la raiz del carpeta una carpeta `input` y una carpeta `output` o cambiar en main.py las variables `input_path` y `output_path`que recogen la ruta de los archivos de entrada y salida.

En la carpeta `input` tendremos que ir metiendo los archivos excel que queremos transformar. Si hay más de un archivo en input siempre se ejecutará sobre el último modificado.

Los dos archivos de salida contendrán en su nombre el mes y año de los datos que contiene el excel, de tal manera que si queremos actualizar el archivo de un mes en cuestión, sólo tenemos que meter en `input` el excel del mes actualizado y ejecutar el programa.

Para ejecutar el programa nos situaremos en la carpeta raiz a través del terminal y ejecutaremos la siguiente línea
`python main.py`


## Columnas: 
- Para la parte del **1414**:
    - fecha
    - conv_llam_netas
    - aaee_llam_netas
    - mail_envios
    - mail_llam_netas
    - carrefour_llam_netas
    - sms_envios
    - sms_llam_netas
    - transf_llam_netas
    - est_llam_netas
    - tot_llam_netas
    - vtas_movil
    - vtas_fijo
    - sheet (dimensión que permite diferenciar entre empresa y residencial)
    - radio_llam_netas
- Para la parte de **teleweb**:
    - fecha
    - est_llam_netas
    - tot_llam_netas
    - vtas_movil_tw
    - vtas_fijo_tw
    - vtas_movil_web
    - vtas_fijo_web
    - sheet




