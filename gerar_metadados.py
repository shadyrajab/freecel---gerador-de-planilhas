import pandas as pd 

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def gerar_metadados_movel(month):

    df_movel = pd.read_excel(f'{month}/móvel/Móvel - {month} - Papuda.xlsx')

    tipo_venda = pd.DataFrame(df_movel['TIPO VENDA'].value_counts())

    tipo_venda.to_excel(f'{month}/metadados/Metadados - Móvel - {month}.xlsx')
    


def gerar_metadados_fixa(month):

    df_fixa = pd.read_excel(f'{month}/fixa e avançada/Fixa e Avançada - {month} - Papuda.xlsx')

    tipo_venda = pd.DataFrame(df_fixa['TIPO DE VENDA'].value_counts())

    tipo_venda.to_excel(f'{month}/metadados/Metadados - Fixa - {month}.xlsx')


for month in months:
    gerar_metadados_movel(month)
    gerar_metadados_fixa(month)