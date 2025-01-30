import tkinter as tk

def open_login():
    login_root = tk.Tk()
    login_root.title("Login")

    largura_janela = 300
    altura_janela = 150
    largura_tela = login_root.winfo_screenwidth()
    altura_tela = login_root.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    login_root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    tk.Label(login_root, text="Nome do Cliente:").pack(pady=5)
    client_entry = tk.Entry(login_root)
    client_entry.pack(pady=5)

    def on_login():
        client = client_entry.get().strip()
        if client:
            login_root.destroy()
            from send_screen import open_main_app  # Importação dentro da função para evitar importação circular
            open_main_app(client)

    login_button = tk.Button(login_root, text="Entrar", command=on_login)
    login_button.pack(pady=10)
    
    login_root.mainloop()
