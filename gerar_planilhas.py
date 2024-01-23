import pandas as pd 

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
index_fixa = ['UF',  'CNPJ', 'TIPO DE VENDA', 'QUANTIDADE DE PRODUTOS', 'GESTOR',	'VALOR DO PLANO', 'CONSULTOR', 'REVENDA', 'RK_TP_FIXA', 'RK_TP_AVANCADA', 'RK_ST_ATIVO', 'RK_ST_VVN', 'RK_ST_F1_GANHA']
index_movel = ['UF',  'CNPJ/CPF',  'PLANO', 'TIPO VENDA', 'VALOR DO PLANO', 'QTD SERVIÇOS', 'REVENDA', 'CONSULTOR', 'GESTOR', 'RK_TP_ALTAS', 'RK_TP_MIGRACOES', 'RK_TP_MIGRACOES_PRE_POS', 'RK_ST_PARCIAIS', 'RK_ST_CONSOLIDADO']

def movel(month):
    df_movel = pd.read_excel(f'{month}/móvel/Móvel - {month} - Papuda.xlsx')

    df_movel = df_movel[(df_movel['STATUS'] == 'CONCLUIDO') & (df_movel['QTD SERVIÇOS'] > 0)]
    df_movel = df_movel[index_movel]

    df_movel.to_excel(f'./{month}/móvel/Móvel - Concluidas - {month}.xlsx')

    altas = df_movel[df_movel['RK_TP_ALTAS'] == True]
    migracao_pre_pos = df_movel[df_movel['RK_TP_MIGRACOES_PRE_POS'] == True]

    altas.to_excel(f'./{month}/móvel/Altas Móvel - {month}.xlsx')
    migracao_pre_pos.to_excel(f'./{month}/móvel/Migração pré pós Móvel - {month}.xlsx')

def fixa(month):
    df_fixa = pd.read_excel(f'{month}/fixa e avançada/Fixa e Avançada - {month} - Papuda.xlsx')

    df_fixa = df_fixa[(df_fixa['STATUS'] == 'ATIVO') & (df_fixa['QUANTIDADE DE PRODUTOS'] > 0)]
    df_fixa = df_fixa[index_fixa]

    df_fixa.to_excel(f'{month}/fixa e avançada/Fixa e Avançada - Concluidas - {month}.xlsx')

    avancada = df_fixa[df_fixa['RK_TP_AVANCADA'] == True]
    soho = df_fixa[df_fixa['RK_TP_FIXA'] == True]
    vvn = df_fixa[df_fixa['RK_ST_VVN'] == True]

    avancada.to_excel(f'{month}/fixa e avançada/Avançada - {month}.xlsx')
    soho.to_excel(f'{month}/fixa e avançada/Soho - {month}.xlsx')
    vvn.to_excel(f'{month}/fixa e avançada/VVN - {month}.xlsx')

for month in months:
    movel(month)
    fixa(month)