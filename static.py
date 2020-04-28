# Columnas por pestaña que mantenemos en el archivo final
res_1414_cols_to_keep = [0, 5, 13, 22, 23, 24, 25, 26, 29, 37, 38, 49, 50, 53, 54]
emp_1414_cols_to_keep = [0, 1, 7, 12, 16, 17, 19, 20, 23, 24, 26, 27]
res_tw_cols_to_keep = [0, 1, 2, 13, 14, 16, 17, 18, 19, 21, 22]
emp_tw_cols_to_keep = [0, 1, 2, 5, 6, 8, 9, 10 , 11, 13, 14]

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
    'Est. Móvil':'est_vtas_movil',
    'Real Móvil': 'vtas_movil',
    'Est. Fijo':'est_vtas_fijo',
    'Real Fijo': 'vtas_fijo'
}

emp_1414_cols = {
    'Fecha ': 'fecha',
    'Llam. Netas': 'conv_llam_netas',
    'Llamadas Netas': 'aaee_llam_netas',
    'Llamadas': 'radio_llam_netas',
    'Envíos' : 'sms_envios',
    'Total Llamadas': 'sms_llam_netas',
    'Est. Llam. Netas': 'est_llam_netas',
    'Llam. Netas.1': 'tot_llam_netas',
    'Est. Móvil':'est_vtas_movil',
    'Real Móvil': 'vtas_movil',
    'Est. Fijo':'est_vtas_fijo',
    'Real Fijo': 'vtas_fijo'
}

## res_tw_cols se usará tanto en residencial teleweb como en empresas teleweb
res_tw_cols = {
    'FECHA': 'fecha',
    'Estimación': 'est_llam_netas',
    'REALES': 'tot_llam_netas',
    'Estimación Total Canal Online':'est_vtas_movil_tot',
    'Real Total Canal Online': 'vtas_mov_tot',
    'Real Teleweb': 'vtas_movil_tw',
    'Real Teleweb+Web': 'vtas_movil_tw_web',
    'Estimación Total Canal Online.1':'est_vtas_fijo_tot',
    'Real Total Canal Online.1': 'vtas_fijo_tot',
    'Real Teleweb.1': 'vtas_fijo_tw',
    'Real Teleweb+Web.1': 'vtas_fijo_tw_web'
}
