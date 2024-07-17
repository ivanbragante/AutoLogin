import pyautogui
import time
import keyboard
import webbrowser
import os
import datetime
from esc_encerra import check_for_esc
from gui import guid_, id_tc, senha_tc, senha_ramal, ramal, senha_cy, senha_en
import subprocess
import pygetwindow as gw

# função em abrirNav.py
def set_config(g, id_t, senha_t, senha_r, ram, senha_c, senha_e):
    global guid_, id_tc, senha_tc, senha_ramal, ramal, senha_cy, senha_en
    guid_ = g
    id_tc = id_t
    senha_tc = senha_t
    senha_ramal = senha_r
    ramal = ram
    senha_c = senha_c
    senha_e = senha_e

# guid = ''
# id_tc = ''
# senha_tc = ''
# senha_ramal = ''
# ramal = ''
# senha_cy = ''
# senha_en = ''

def abrir_c():
    caminho_cisco = r"C:caminho do programa"
    time.sleep(1)
    os.startfile(caminho_cisco) # Abre o arquivo .exe
    time.sleep(1)
    pyautogui.typewrite(senha_en)

def maximiza():
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
    time.sleep(2)
    subprocess.Popen([chrome_path, "--new-window", "about:blank"])
    # Aguardar um pouco para a janela abrir
    time.sleep(1)
    #Encontrar a janela do Chrome
    windows = gw.getWindowsWithTitle('about:blank - Google Chrome')
    time.sleep(1.5)
    if windows:
        window = windows[0]
        time.sleep(1.5)
        window.maximize()  # Maximiza a janela
    else:
        print("Janela do Chrome não encontrada.")

#batendo o ponto
def b_p():
    global id_t
    global senha_t
    webbrowser.open('site 1')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(17)
    for _ in range (5):
        time.sleep(0.4)
        pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(id_tc)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(senha_tc)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab') 
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('enter')

#logando no cisco
def login_c(): 
    global guid
    global senha_ramal
    global ramal
    check_for_esc()
    webbrowser.open('site 2')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(3.5)
    check_for_esc()
    pyautogui.typewrite(guid) #login
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.3)
    pyautogui.typewrite(senha_ramal) #senha
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('tab')
    check_for_esc()
    pyautogui.typewrite(ramal) #ramal
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('tab') 
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('enter') #Enter para logar
    time.sleep(4)
    pyautogui.hotkey('enter') #Enter para clicar no status
    check_for_esc()
    time.sleep(0.5)
    pyautogui.keyDown('shift')
    for _ in range(1):
        pyautogui.hotkey('tab') #Selecionar status
        time.sleep(0.8)
    pyautogui.keyUp('shift')
    pyautogui.hotkey('tab') #Seleciona available
    time.sleep(0.4)
    pyautogui.hotkey('enter') #Fica available
    
    
def abrir_schat():
    webbrowser.open('site 3')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(7)
    for _ in range(3):
        pyautogui.hotkey('tab') #Selecionar status
        time.sleep(0.3)
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('enter') #clica em available
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('esc')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'shift', 'i') #abre o console
    check_for_esc()
    time.sleep(1.5)
    pyautogui.hotkey('enter')
    time.sleep(1)
    js_command = 'refreshlaunch = window.open("https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"); timerScreen = setInterval(function(){refreshlaunch.location.href="https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"}, 18000);'
    pyautogui.typewrite(js_command) #liga a atualização do chat automatico
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(1.3)

def gchat():
    webbrowser.open('https://chat.google.com/')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.7)

def cy():
    global guid
    global senha_cy
    webbrowser.open('site 4')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(8)
    pyautogui.typewrite(guid) #login
    time.sleep(0.4)
    pyautogui.hotkey('tab')
    pyautogui.typewrite(senha_cy) #senha
    time.sleep(0.4)

def open_e():
    global senha_en
    # Caminho para o arquivo .exe que você deseja abrir
    caminho_en = r"C:\\caminho programa 2"
    time.sleep(1)
    os.startfile(caminho_en) # Abre o arquivo .exe
    time.sleep(1)
    pyautogui.typewrite(senha_en)