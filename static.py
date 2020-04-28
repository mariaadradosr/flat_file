# Columnas por pestaña que mantenemos en el archivo final
res_1414_cols_to_keep = [0, 5, 13, 22, 23, 24, 25, 26, 29, 37, 38, 50, 54]
emp_1414_cols_to_keep = [0, 1, 7, 12, 17, 19, 20, 24, 27]
res_tw_cols_to_keep = [0, 1, 2, 16, 17, 21, 22]
emp_tw_cols_to_keep = [0, 1, 2, 8, 9, 13, 14]

# Mapeo nombre columnas
res_1414_cols = {
    'FECHA': 'fecha',
    'Llam. Netas': 'conv_llam_netas',
    'Llam. Netas.1': 'aaee_llam_netas',
    'Envíos': 'mail_envios',
    'Llam. Netas.2': 'mail_llam_netas',
    'Llamadas': 'carrefour_llam_netas',
    'Envíos.1': 'sms_envios',
    'Total Llamadas': 'sms_llam_netas',
    'Total Llamadas.1': 'transf_llam_netas',
    'Est. Llam. Netas': 'est_llam_netas',
    'Llam. Netas.3': 'tot_llam_netas',
    'Real Móvil': 'vtas_movil',
    'Real Fijo': 'vtas_fijo'
}

emp_1414_cols = {
    'Fecha ': 'fecha',
    'Llam. Netas': 'conv_llam_netas',
    'Llamadas Netas': 'aaee_llam_netas',
    'Llamadas': 'radio_llam_netas',
    'Total Llamadas': 'sms_llam_netas',
    'Est. Llam. Netas': 'est_llam_netas',
    'Llam. Netas.1': 'tot_llam_netas',
    'Real Móvil': 'vtas_movil',
    'Real Fijo': 'vtas_fijo'
}

## res_tw_cols se usará tanto en residencial teleweb como en empresas teleweb
res_tw_cols = {
    'FECHA': 'fecha',
    'Estimación': 'est_llam_netas',
    'REALES': 'tot_llam_netas',
    'Real Teleweb': 'vtas_movil_tw',
    'Real Teleweb+Web': 'vtas_movil_tw_web',
    'Real Teleweb.1': 'vtas_fijo_tw',
    'Real Teleweb+Web.1': 'vtas_fijo_tw_web'
}
