import time
import webbrowser
from gui import show_gui
from abrirNav import maximiza, b_p, abrir_schat, login_c, cy, open_e, gchat, set_config, abrir_c
from gui import guid_, id_tc, senha_tc, senha_ramal, ramal, senha_cy, senha_en

def execute_selected_functions(selected_functions):

    if selected_functions['bate_ponto']:
        b_p()

    if selected_functions['login_cisco']:
        login_c()
    
    if selected_functions['abrir_snowchat']:
        abrir_schat()

    if selected_functions['gchat']:
        gchat()
    
    if selected_functions['cyberark']:
        cy()

    if selected_functions['open_entrust']:
        open_e()
    
    print("Tarefas executadas com sucesso!")

def main():
    selected_functions, guid, id_tcs, senha_tcs, senha_ramal, senha_cyber, senha_entrust, ramal = show_gui()
    if selected_functions:
        abrir_c()
        time.sleep(2)
        maximiza()
        set_config(guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust)
        execute_selected_functions(selected_functions)
        
    else:
        print("Nenhuma tarefa foi selecionada para execução.")
    
if __name__ == "__main__":
    main()