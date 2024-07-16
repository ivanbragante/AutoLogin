import pyautogui
import time






import keyboard






import webbrowser
import os






import datetime






from esc_encerra import check_for_esc






from gui import guid, id_, senha_, senha_ramal, ramal, senha_c, senha_e






import subprocess






import pygetwindow as gw






# função em abrirNav.py






def set_config(g, id_t, senha_t, senha_r, ram, senha_c, senha_e):





    global guid, id_, senha_, senha_ramal, ramal, senha_c, senha_e





    guid = g





    id_ = id_t





    senha_tcs = senha_t





    senha_ramal = senha_r





    ramal = ram





    senha_cyber = senha_c





    senha_entrust = senha_e






def abrir_c():





    caminho_cis = r"C:\\caminho do app"





    time.sleep(1)





    os.startfile(caminho_cis)  # Abre o arquivo .exe





    time.sleep(1)


    pyautogui.typewrite(senha_e)






def maximiza():





    # ajuste o caminho conforme necessário




    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"





    time.sleep(2)





    subprocess.Popen([chrome_path, "--new-window", "about:blank"])





    # Aguardar um pouco para a janela abrir





    time.sleep(1)





    # Encontrar a janela do Chrome





    windows = gw.getWindowsWithTitle('about:blank - Google Chrome')





    time.sleep(1.5)





    if windows:





        window = windows[0]





        time.sleep(1.5)





        window.maximize()  # Maximiza a janela





    else:





        print("Janela do Chrome não encontrada.")







def bat_p():





    global id_





    global senha_





    webbrowser.open('site 1')





    time.sleep(1)



    pyautogui.hotkey('enter')





    check_for_esc()





    time.sleep(17)





    for _ in range(5):





        time.sleep(0.4)





        pyautogui.hotkey('tab')





    check_for_esc()





    time.sleep(0.2)





    pyautogui.typewrite(id_)





    check_for_esc()





    time.sleep(0.2)





    pyautogui.hotkey('tab')





    check_for_esc()





    time.sleep(0.2)


    pyautogui.typewrite(senha_)





    check_for_esc()





    time.sleep(0.2)





    pyautogui.hotkey('tab')





    check_for_esc()





    time.sleep(0.3)



    pyautogui.hotkey('enter')






# logando no cisco






def login_c():





    global guid





    global senha_ramal





    global ramal





    check_for_esc()





    webbrowser.open(




        'site 2')





    time.sleep(1)



    pyautogui.hotkey('enter')





    check_for_esc()





    time.sleep(3.5)





    check_for_esc()





    pyautogui.typewrite(guid)  # login





    check_for_esc()





    time.sleep(0.2)





    pyautogui.hotkey('tab')





    check_for_esc()





    time.sleep(0.3)





    pyautogui.typewrite(senha_ramal)  # senha





    check_for_esc()





    time.sleep(0.3)





    pyautogui.hotkey('tab')





    check_for_esc()





    pyautogui.typewrite(ramal)  # ramal





    check_for_esc()





    time.sleep(0.3)





    pyautogui.hotkey('tab')





    check_for_esc()





    time.sleep(0.3)





    pyautogui.hotkey('enter')  # Enter para logar





    time.sleep(4)





    pyautogui.hotkey('enter')  # Enter para clicar no status





    check_for_esc()





    time.sleep(0.5)





    pyautogui.keyDown('shift')





    for _ in range(1):





        pyautogui.hotkey('tab')  # Selecionar status





        time.sleep(0.8)





    pyautogui.keyUp('shift')





    pyautogui.hotkey('tab')  # Seleciona available





    time.sleep(0.4)





    pyautogui.hotkey('enter')  # Fica available






def abrir_snowchat():





    webbrowser.open('site 3')





    time.sleep(1)



    pyautogui.hotkey('enter')





    check_for_esc()





    time.sleep(7)





    for _ in range(3):





        pyautogui.hotkey('tab')  # Selecionar status





        time.sleep(0.3)





    check_for_esc()





    time.sleep(0.5)





    pyautogui.hotkey('enter')  # clica em available





    check_for_esc()





    time.sleep(0.5)



    pyautogui.hotkey('enter')





    check_for_esc()





    time.sleep(0.5)



    pyautogui.hotkey('esc')





    time.sleep(0.6)





    pyautogui.hotkey('ctrl', 'shift', 'i')  # abre o console





    check_for_esc()





    time.sleep(1.5)



    pyautogui.hotkey('enter')





    time.sleep(1)





    js_command = 'refreshlaunch = window.open("https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"); timerScreen = setInterval(function(){refreshlaunch.location.href="https://wwwpwcnetwork.pwc.myshn.net/now/workspace/agent/inbox"}, 18000);' # atualização da página automatica





    pyautogui.typewrite(js_command)  # liga o chat automatico





    check_for_esc()





    time.sleep(0.5)



    pyautogui.hotkey('enter')





    time.sleep(1.3)






def gchat():





    webbrowser.open('https://chat.google.com/')





    time.sleep(0.5)



    pyautogui.hotkey('enter')





    time.sleep(0.7)






def cyber():





    global guid





    global senha_c





    webbrowser.open('site 4')





    time.sleep(1)



    pyautogui.hotkey('enter')





    check_for_esc()





    time.sleep(8)





    pyautogui.typewrite(guid)  # login





    time.sleep(0.4)





    pyautogui.hotkey('tab')





    pyautogui.typewrite(senha_c)  # senha





    time.sleep(0.4)






def open_en():





    global senha_e





    # Caminho para o arquivo .exe que você deseja abrir





    caminho_entrust = r"C:\\caminho app"





    time.sleep(1)





    os.startfile(caminho_entrust)  # Abre o arquivo .exe





    time.sleep(1)


    pyautogui.typewrite(senha_e)




