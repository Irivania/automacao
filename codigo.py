# BIBLIOTECAS = PACOTES DE CÓDIGOS
# pyautogui = biblioteca para automação de tarefas
# PASSO A PASSO PARA CADASTRAR PRODUTOS EM UM SITE
import pyautogui
import time
import subprocess
import pandas
pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('microsoft edge')   
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
# fazer uma pausa para o site carregar
pyautogui.sleep(3)

# passo 02: FAZER LOGIN
pyautogui.click(x=439, y=368) # clicar no campo de email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab') # ir para o campo de senha
pyautogui.write("sua senha muito muito dificilima") # digitar a senha
pyautogui.press('enter') # clicar no botão de login

# passo 03: ABRIR A BASE DE DADOS
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    # passo 04: CADASTRAR OS PRODUTOS
    pyautogui.click(x=500, y=246)   # clicar no campo do código
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo) # digitar o código do produto
    pyautogui.press('tab') # ir para o campo do nome

    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca) # digitar o nome do marca   
    pyautogui.press('tab') # ir para o campo tipo de produto

    #tipo de produto
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo) # digitar o tipo de produto
    pyautogui.press('tab') # ir para o campo categoria de produto

    #categoria de produto
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria) # digitar categoria de produto
    pyautogui.press('tab') # ir para o campo preço de custo 

    #preço de unitário
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])   
    pyautogui.write(str(preco_unitario)) # digitar o preço de unitário
    pyautogui.press('tab') # ir para o campo preço de venda

    #preço CAHA000251de venda de custo   
    preco_venda = str(tabela.loc[linha, 'custo'])
    pyautogui.write(preco_venda) # digitar o preço de custo
    pyautogui.press('tab') # ir para o campo observação

    #observação
    obs = str(tabela.loc[linha, 'obs'])     
    if obs != 'nan': 
        pyautogui.write("Mouse sem fio") # digitar a observação
    pyautogui.press('enter') # clicar no botão de cadastrar

    # enviar
    pyautogui.press('enter') # clicar no botão de cadastrar

# voltar para a tela inicial
pyautogui.scroll(6000)


