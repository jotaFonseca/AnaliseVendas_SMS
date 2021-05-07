import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC3c9a69fb9d8bcb6e808f2501938f82d3"
# Your Auth Token from twilio.com/console
auth_token = "95b961f6ae581ba61fa73677104ead6d"

client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendendor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes},alguém bateu a meta de R$55.000,00. Vendedor: {vendendor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5521985650273",
            from_="+19735641745",
            body=f'No mês de {mes},alguém bateu a meta de R$55.000,00. Vendedor: {vendendor}, Vendas: {vendas}')
        print(message.sid)
