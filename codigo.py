# BIBLIOTECAS = PACOTES DE CÓDIGOS
# pyautogui = biblioteca para automação de tarefas
# PASSO A PASSO PARA CADASTRAR PRODUTOS EM UM SITE
import pyautogui
import time
import subprocess
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
subprocess.Popen(r'C:\Users\Usuário\Documents\automacao\base_de_dados.xlsx')

# passo 04: CADASTRAR OS PRODUTOS
# passo 05: REPETIR O PROCESSO ATÉ O ÚLTIMO PRODUTO


