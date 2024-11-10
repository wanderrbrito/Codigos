"""
Codigos usados para testar a integracao com o Telegram
Configurando a API e explorando os dados
"""

# Importando as bibliotecas que  serão usadas
from getpass import getpass
import json
import requests
from datetime import datetime
import pyarrow as pa

# Configurando a API do Telegram
token = getpass()
base_url = f'https://api.telegram.org/bot{token}'

# Usando método "gwtMe" para confirmar as informacoes do grupo
response = requests.get(url=f'{base_url}/getMe')
print(f'{base_url}/getMe')

print(json.dumps(json.loads(response.text), indent=2))

# Usando método "getUopdates" para exibir as mensagens recebidas pela API
response = requests.get(url=f'{base_url}/getUpdates')

print(json.dumps(json.loads(response.text), indent=2))

import json

with open('telegram.json', mode='r', encoding='utf8') as fp:
  data = json.load(fp)
  data = data["message"]

"""
Iterando sobre as mensagens recebidas para coletar das chaves do arquivo para selecionar os dados de interesse.
Caso a mensagem não possua a chave text, será atribuido o valor None.
Adcionando tambem duas chaves de tempo para indicar quando o dado foi processado:
""" 
parsed_data = dict()

for key, value in data.items():

    if key == 'from':
        for k, v in data[key].items():
            if k in ['id', 'is_bot', 'first_name']:
              parsed_data[f"{key if key == 'chat' else 'user'}_{k}"] = [v]

    elif key == 'chat':
        for k, v in data[key].items():
            if k in ['id', 'type']:
              parsed_data[f"{key if key == 'chat' else 'user'}_{k}"] = [v]

    elif key in ['message_id', 'date', 'text']:
        parsed_data[key] = [value]

if not 'text' in parsed_data.keys():
  parsed_data['text'] = [None]

parsed_data['context_date'] = [date]
parsed_data['context_timestamp'] = [timestamp]

# Visualizando as mensagens coletadas
for k, v in parsed_data.items():
  print(f"{k}: {v}")

# Usando o  PyArrow para criar uma tabela com os dados processado. que pode convertido em um arquivo no formato Apache Parquet.
table = pa.Table.from_pydict(mapping=parsed_data)
table()