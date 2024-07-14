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


def maximiza():
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # ajuste o caminho conforme necessário
    # Abrir uma nova janela vazia
    subprocess.Popen([chrome_path, "--new-window", "about:blank"])
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2.5)
    subprocess.Popen([chrome_path, "--new-window", "about:blank"])
    # Aguardar um pouco para a janela abrir
    time.sleep(1.5)
    # Encontrar a janela do Chrome
    windows = gw.getWindowsWithTitle('about:blank - Google Chrome')  # Tente 'Chrome' em vez de 'Nova janela'
    time.sleep(1.5)
    if windows:
        window = windows[0]
        window.moveTo(700, 331)  # Move para o meio do monitor principal
        time.sleep(1.5)
        pyautogui.hotkey('win', 'up')
        time.sleep(0.5)
        window.maximize()  # Maximiza a janela
    else:
        print("Janela do Chrome não encontrada.")

#batendo o ponto
def bate_ponto():
    global id_tcs
    global senha_tcs
    webbrowser.open('https://cliente.apdata.com.br/dicon/index.html')
    time.sleep(2)
    check_for_esc()
    time.sleep(17)
    pyautogui.click(136, 648)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(id_tcs)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.click(122, 672)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(senha_tcs)
    check_for_esc()
    time.sleep(0.2)
    pyautogui.click(127, 698) #bate o ponto  
    check_for_esc()
    time.sleep(4)

#logando no cisco
def login_cisco(): 
    global guid
    global senha_ramal
    global ramal
    check_for_esc()
    webbrowser.open('https://uccx01.pwc.intcloud.com.br:8445/desktop/container/?locale=pt_BR')
    check_for_esc()
    time.sleep(7)
    pyautogui.click(672, 400)
    check_for_esc()
    pyautogui.typewrite(guid) #login
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab')
    check_for_esc()
    time.sleep(0.2)
    pyautogui.typewrite(senha_ramal) #senha
    check_for_esc()
    time.sleep(0.2)
    pyautogui.hotkey('tab')
    check_for_esc()
    pyautogui.typewrite(ramal) #ramal
    check_for_esc()
    time.sleep(0.2)
    pyautogui.click(672, 604) #Clique para logar
    check_for_esc()
    time.sleep(4)
    pyautogui.click(378, 139) #Clica no status
    check_for_esc()
    time.sleep(0.4)
    pyautogui.click(378, 178)
    check_for_esc()
    time.sleep(0.4)
    pyautogui.click(628, 390) #ficar available 
    check_for_esc()   
    
def abrir_snowchat():
    webbrowser.open('https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox')
    check_for_esc()
    time.sleep(14)
    pyautogui.click(97, 229) #clica no status
    check_for_esc()
    time.sleep(0.4)
    pyautogui.click(97, 248) #clica em available
    check_for_esc()
    time.sleep(0.4)
    pyautogui.click(359, 320) #clica em branco
    check_for_esc()
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'shift', 'i') #abre o console
    check_for_esc()
    time.sleep(1.5)
    js_command = 'refreshlaunch = window.open("https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"); timerScreen = setInterval(function(){refreshlaunch.location.href="https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"}, 18000);'
    pyautogui.typewrite(js_command) #liga o chat automatico
    check_for_esc()
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(1.3)

def bom_dia():
    webbrowser.open('https://chat.google.com/')
    check_for_esc()
    time.sleep(5)
    pyautogui.click(99, 523) #clica no grupo
    check_for_esc()
    time.sleep(3.5)
    pyautogui.click(549, 653) #clica pra escrever a mensagem
    check_for_esc()
    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime("%d/%m")
    saudacao = "Bom dia "
    mensagem = saudacao + data_formatada
    time.sleep(0.5)
    pyautogui.typewrite(mensagem)
    check_for_esc()
    time.sleep(0.3)
    pyautogui.hotkey('enter')   
    check_for_esc() 
    time.sleep(1.5)

def cyberark():
    global guid
    global senha_cyber
    webbrowser.open('https://paa.pum.pwcinternal.com/PasswordVault/v10/logon/cyberark')
    check_for_esc()
    time.sleep(7)
    pyautogui.click(661, 544)
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
    
def gchat():
    caminho_gchat = r"C:\\Users\\ibragante001\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\apps do Chrome\\Google Chat.lnk"
    time.sleep(1)
    os.startfile(caminho_gchat) # Abre o arquivo gchat