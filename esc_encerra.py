import keyboard

def check_for_esc():
            if keyboard.is_pressed('esc'):
                print("Execução interrompida pelo usuário.")
                raise KeyboardInterrupt