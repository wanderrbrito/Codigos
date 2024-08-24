"""
Codigo do projeto de automacao de tarefas usando Pyautogui
Projeto construido durante a jornada Python da Hastag Treinamentos
"""
import pyautogui
import time
import pandas as pd
from pegar_posicao import posicao
pyautogui.PAUSE = 0.3

# abrir o navegador e digitar o endereco do site
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')

# time.sleep(3)
# # selecionar e preencger o campo login
# pyautogui.click(posicao)
# pyautogui.write('wanderbola@orion.com')

# pyautogui.press('tab')   

# # preencher o campo senha
# pyautogui.write('stargate')         
# pyautogui.press('tab')
# pyautogui.press('enter')    

# tabela = pd.read_csv('produtos.csv')
# print(tabela)


# for linha in tabela.index:
#     # clicar no campo de código
#     pyautogui.click(x=554, y=276)
#     # pegar da tabela o valor do campo que a gente quer preencher
#     codigo = tabela.loc[linha, "codigo"]
#     # preencher o campo
#     pyautogui.write(str(codigo))
#     # passar para o proximo campo
#     pyautogui.press("tab")
#     # preencher o campo
#     pyautogui.write(str(tabela.loc[linha, "marca"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "tipo"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "categoria"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))                           
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "custo"]))
#     pyautogui.press("tab")
#     obs = tabela.loc[linha, "obs"]
#     if not pd.isna(obs):
#         pyautogui.write(str(tabela.loc[linha, "obs"]))
#     pyautogui.press("tab")
#     pyautogui.press("enter") # cadastra o produto (botao enviar)
#     # dar scroll de tudo pra cima
#     pyautogui.scroll(5000)
#     # Passo 5: Repetir o processo de cadastro até o fim