import pyautogui
import time
import keyboard
import webbrowser
import os
import datetime
from esc_encerra import check_for_esc
from gui import guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust
import subprocess
import pygetwindow as gw

# função em abrirNav.py
def set_config(g, id_t, senha_t, senha_r, ram, senha_c, senha_e):
    global guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust
    guid = g
    id_tcs = id_t
    senha_tcs = senha_t
    senha_ramal = senha_r
    ramal = ram
    senha_cyber = senha_c
    senha_entrust = senha_e

def abrir_cisco():
    caminho_cisco = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Cisco Jabber\\Cisco Jabber.lnk"
    time.sleep(1)
    os.startfile(caminho_cisco) # Abre o arquivo .exe
    time.sleep(1)
    pyautogui.typewrite(senha_entrust)

def maximiza():
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # ajuste o caminho conforme necessário
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
def bate_ponto():
    global id_tcs
    global senha_tcs
    webbrowser.open('https://cliente.apdata.com.br/dicon/index.html')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(17)
    for _ in range (5):
        time.sleep(0.4)
        pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(id_tcs)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(senha_tcs)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab') 
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('enter')

#logando no cisco
def login_cisco(): 
    global guid
    global senha_ramal
    global ramal
    check_for_esc()
    webbrowser.open('https://uccx01.pwc.intcloud.com.br:8445/desktop/container/?locale=pt_BR')
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
    
    
def abrir_snowchat():
    webbrowser.open('https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox')
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
    pyautogui.typewrite(js_command) #liga o chat automatico
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(1.3)

def gchat():
    webbrowser.open('https://chat.google.com/')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.7)

def cyberark():
    global guid
    global senha_cyber
    webbrowser.open('https://paa.pum.pwcinternal.com/PasswordVault/v10/logon/cyberark')
    time.sleep(1)
    pyautogui.hotkey('enter')
    check_for_esc()
    time.sleep(8)
    pyautogui.typewrite(guid) #login
    time.sleep(0.4)
    pyautogui.hotkey('tab')
    pyautogui.typewrite(senha_cyber) #senha
    time.sleep(0.4)

def open_entrust():
    global senha_entrust
    # Caminho para o arquivo .exe que você deseja abrir
    caminho_entrust = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Entrust\\Entrust Identity Desktop Soft Token.lnk"
    time.sleep(1)
    os.startfile(caminho_entrust) # Abre o arquivo .exe
    time.sleep(1)
    pyautogui.typewrite(senha_entrust)