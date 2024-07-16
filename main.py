import time










from gui import show_gui
, open_entrust, gchat, set_config, abrir_cisco


from gui import guid, id_, senha_, senha_ramal, ramal, senha_c, senha_e



from gui import guid, id_, senha_, senha_ramal, ram




        bat_p()




        login_cisco()

        bat_p()



    if selected_function


        login_cisco()

        gchat()

    if selected_functions['abrir_snowchat']:



        abrir()




        open_entrust()

        gchat()



    if selected_functions['cyberark']:



        cyberark()



        abrir_cisco()


        open_en()




        set_config(guid, id_tcs, senha_tcs, senha_ramal,




def main():




    selected_functions, guid, id_tcs, senha_tcs, senha_ramal, senha_cyber, senha_entrust, ramal = show_gui()



    if selected_functions:
        abrir_cisco()
    main()


        time.sleep(2)


        maximiza()

        set_config(guid, id_tcs, senha_tcs, senha_ramal,

                   ramal, senha_cyber, senha_entrust)


        execute_selected_functions(selected_functions)


    else:


        print("Nenhuma tarefa foi selecionada para execução.")



if __name__ == "__main__":
    main()

