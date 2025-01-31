import tkinter as tk
from PIL import Image, ImageTk
from assets.func.login.registration_users import *
from assets.func.interface.config_page_tk import config_page_tk


def open_login():
    """Abre a janela de login."""

    # Verifica se há um usuário logado e inicia a aplicação principal automaticamente
    usuario_logado = carregar_sessao()
    if usuario_logado:
        from assets.interface.send_screen import open_main_app 
        open_main_app(usuario_logado)
        return

    # Criar a janela de login
    login_root = tk.Tk()
    login_root.title("Login")

    config_page_tk(300,150, login_root)

    tk.Label(login_root, text="Nome do Cliente:").pack(pady=5)
    client_entry = tk.Entry(login_root)
    client_entry.pack(pady=5)

    def on_login():       
        client = client_entry.get().strip()
        
        if client:
            from assets.interface.send_screen import open_main_app  # Função para abrir a tela principal
            user = autenticar_usuario(client.upper())
            login_root.destroy()
            open_main_app(user)

    login_button = tk.Button(login_root, text="Entrar", command=on_login)
    login_button.pack(pady=10)

    login_root.mainloop()
