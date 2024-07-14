import time
import webbrowser
from gui import show_gui
from abrirNav import maximiza, bate_ponto, abrir_snowchat, bom_dia, login_cisco, cyberark, open_entrust, gchat, set_config
from gui import guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust
from esc_encerra import check_for_esc

def execute_selected_functions(selected_functions):

    if selected_functions['bate_ponto']:
        bate_ponto()
    # check_for_esc()

    if selected_functions['login_cisco']:
        login_cisco()
    # check_for_esc()
    
    if selected_functions['abrir_snowchat']:
        abrir_snowchat()
    # check_for_esc()
    
    if selected_functions['bom_dia']:
        bom_dia()
    # check_for_esc()
    
    if selected_functions['cyberark']:
        cyberark()
    # check_for_esc()

    if selected_functions['open_entrust']:
        open_entrust()
    
    if selected_functions['gchat']:
        gchat()

    print("Tarefas executadas com sucesso!")

def main():
    selected_functions, guid, id_tcs, senha_tcs, senha_ramal, senha_cyber, senha_entrust, ramal = show_gui()
    if selected_functions:
        maximiza()
        set_config(guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust)
        execute_selected_functions(selected_functions)
        
    else:
        print("Nenhuma tarefa foi selecionada para execução.")
    
if __name__ == "__main__":
    main()