import time
import webbrowser
from gui import show_gui
from abrirNav import maximiza, bate_ponto, abrir_snowchat, login_cisco, cyberark, open_entrust, gchat, set_config, abrir_cisco
from gui import guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust

def execute_selected_functions(selected_functions):

    if selected_functions['bate_ponto']:
        bate_ponto()

    if selected_functions['login_cisco']:
        login_cisco()
    
    if selected_functions['abrir_snowchat']:
        abrir_snowchat()

    if selected_functions['gchat']:
        gchat()
    
    if selected_functions['cyberark']:
        cyberark()

    if selected_functions['open_entrust']:
        open_entrust()
    
    print("Tarefas executadas com sucesso!")

def main():
    selected_functions, guid, id_tcs, senha_tcs, senha_ramal, senha_cyber, senha_entrust, ramal = show_gui()
    if selected_functions:
        abrir_cisco()
        time.sleep(2)
        maximiza()
        set_config(guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust)
        execute_selected_functions(selected_functions)
        
    else:
        print("Nenhuma tarefa foi selecionada para execução.")
    
if __name__ == "__main__":
    main()