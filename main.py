import pandas as pd
from twilio.rest import Client

# Conta SID twilio.com/console
account_sid = "Exemplo_seu_sid"
# Token de autenticação twilio.com/console
auth_token  = "Exemplo_seu_token"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():

        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5521999999999",
            from_="seu_numero_twilcleario",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)