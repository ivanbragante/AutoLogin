import tkinter as tk
from tkinter import messagebox
import json
import os

# Definição das variáveis
guid_ = ''
id_tc = ''
senha_tc = ''
senha_ramal = ''
ramal = ''
senha_cy = ''
senha_en = ''

selected_functions = {}
config_file = "config.json"

def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(config_file, "w") as file:
        json.dump(config, file)

def save_checkbox_states():
    config_data = {
        "b_p": var_b_p.get(),
        "login_c": var_l_c.get(),
        "abrir_chat": var_abrir_chat.get(),
        "gchat": var_gchat.get(),
        "cy": var_c.get(),
        "open_e": var_open_e.get(),
        "guid": guid_,
        "id_t": id_tc,
        "senha_t": senha_tc,
        "senha_ramal": senha_ramal,
        "ramal": ramal,
        "senha_c": senha_cy,
        "senha_e": senha_en
    }
    save_config(config_data)

def show_gui():
    global selected_functions
    global guid_, id_tc, senha_tc, senha_ramal, ramal, senha_cy, senha_en

    # Carregar configurações
    config = load_config()
    guid_ = config.get("guid", "")
    id_tc = config.get("id_t", "")
    senha_tc = config.get("senha_t", "")
    senha_ramal = config.get("senha_ramal", "")
    ramal = config.get("ramal", "")
    senha_cy = config.get("senha_c", "")
    senha_en = config.get("senha_e", "")

    # Inicializar a janela
    root = tk.Tk()
    root.title("BR-SD Auto Login")

    # Obtém a largura e altura da tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Define o tamanho da janela
    window_width = int(screen_width * 0.2)
    window_height = int(screen_height * 0.25)

    # Centraliza a janela na tela
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Variáveis para os checkboxes
    global var_b_p, var_l_c, var_abrir_chat, var_gchat, var_c, var_open_e
    var_b_p = tk.BooleanVar(value=config.get("bate_ponto", True))
    var_l_c = tk.BooleanVar(value=config.get("login_cisco", True))
    var_abrir_chat = tk.BooleanVar(value=config.get("abrir_snowchat", True))
    var_gchat = tk.BooleanVar(value=config.get("gchat", True))
    var_c = tk.BooleanVar(value=config.get("cyberark", True))
    var_open_e = tk.BooleanVar(value=config.get("open_entrust", True))

    # Criação dos checkboxes
    tk.Checkbutton(root, text="Bater Ponto", variable=var_b_p).pack(anchor='w')
    tk.Checkbutton(root, text="Login Cisco", variable=var_l_c).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir Snowchat", variable=var_abrir_chat).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir GChat", variable=var_gchat).pack(anchor='w')
    tk.Checkbutton(root, text="Cyberark", variable=var_c).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir Entrust", variable=var_open_e).pack(anchor='w')

    def on_yes_click():
        global selected_functions
        selected_functions = {
            'bate_p': var_b_p.get(),
            'login_c': var_l_c.get(),
            'abrir_chat': var_abrir_chat.get(),
            'gchat': var_gchat.get(),
            'cy': var_c.get(),
            'open_e': var_open_e.get()
        }
        save_checkbox_states()
        root.quit()

    def on_no_click():
        global selected_functions
        selected_functions = None
        root.quit()

    def open_settings():
        settings_window = tk.Toplevel(root)
        settings_window.title("Configurações")

        # Define o tamanho da janela de configurações
        settings_width = int(screen_width * 0.18)
        settings_height = int(screen_height * 0.4)
        settings_window.geometry(f"{settings_width}x{settings_height}")

        # Carregar configurações
        config = load_config()

        # Campos de entrada
        tk.Label(settings_window, text="GUID:").pack(anchor='w')
        entry_guid = tk.Entry(settings_window, width=23)
        entry_guid.insert(0, config.get("guid", ""))
        entry_guid.pack(anchor='w')

        tk.Label(settings_window, text="Login D:").pack(anchor='w')
        entry_id_t = tk.Entry(settings_window, width=23)
        entry_id_t.insert(0, config.get("id_t", ""))
        entry_id_t.pack(anchor='w')

        tk.Label(settings_window, text="Senha D:").pack(anchor='w')
        entry_senha_t = tk.Entry(settings_window, width=23)
        entry_senha_t.insert(0, config.get("senha_t", ""))
        entry_senha_t.pack(anchor='w')

        tk.Label(settings_window, text="Senha C:").pack(anchor='w')
        entry_senha_ramal = tk.Entry(settings_window, width=23)
        entry_senha_ramal.insert(0, config.get("senha_ramal", ""))
        entry_senha_ramal.pack(anchor='w')

        tk.Label(settings_window, text="Ramal:").pack(anchor='w')
        entry_ramal = tk.Entry(settings_window, width=23)
        entry_ramal.insert(0, config.get("ramal", ""))
        entry_ramal.pack(anchor='w')

        tk.Label(settings_window, text="Senha C:").pack(anchor='w')
        entry_senha_c = tk.Entry(settings_window, width=23)
        entry_senha_c.insert(0, config.get("senha_c", ""))
        entry_senha_c.pack(anchor='w')

        tk.Label(settings_window, text="Senha Entrust:").pack(anchor='w')
        entry_senha_e = tk.Entry(settings_window, width=23)
        entry_senha_e.insert(0, config.get("senha_e", ""))
        entry_senha_e.pack(anchor='w')

        def save_settings():
            global guid_, id_tc, senha_tc, senha_ramal, ramal, senha_cy, senha_en
            guid_ = entry_guid.get()
            id_tc = entry_id_t.get()
            senha_tc = entry_senha_t.get()
            senha_ramal = entry_senha_ramal.get()
            ramal = entry_ramal.get()
            senha_cy = entry_senha_c.get()
            senha_en = entry_senha_e.get()

            # Salvar configurações no arquivo JSON
            config_data = {
                "guid": guid_,
                "id_t": id_tc,
                "senha_t": senha_tc,
                "senha_ramal": senha_ramal,
                "ramal": ramal,
                "senha_c": senha_cy,
                "senha_e": senha_en
            }
            save_config(config_data)
            messagebox.showinfo("Configurações", "Configurações salvas com sucesso!")
            settings_window.destroy()

        save_button = tk.Button(settings_window, text="Save", command=save_settings)
        save_button.place(relx=0.75, rely=0.90, anchor='center')

    gear_button = tk.Button(root, text="⚙️", command=open_settings)
    gear_button.pack(side='right', padx=10)

    yes_button = tk.Button(root, text="Run", command=on_yes_click)
    no_button = tk.Button(root, text="Close", command=on_no_click)

    yes_button.pack(side='left', padx=10, pady=10)
    no_button.pack(side='right', padx=10, pady=10)

    # Adicionando a mensagem no rodapé
    footer = tk.Label(root, text="Created by Ivan", font=("Arial", 8))
    footer.place(relx=0.43, rely=0.88, anchor='center')

    root.mainloop()

    return selected_functions, guid_, id_tc, senha_tc, senha_ramal, senha_cy, senha_en, ramal