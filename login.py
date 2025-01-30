import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
from assets.func.utils.pop_up import show_popup

# Função de validação de login
def validar_login():
    user = entry_user.get()
    senha = entry_senha.get()

    # Aqui você pode substituir pela lógica de validação real
    if user == "braga" and senha == "123":
        root.destroy()  # Fecha a janela de login
        # Passa o argumento 'client' para o main.py ao abrir
        subprocess.run([sys.executable, "main.py", user])
    else:
        messagebox.showerror("Erro", "user ou senha inválidos")
        show_popup("user ou senha inválidos")

# Criação da janela
root = tk.Tk()
root.title("nZap Login")
root.geometry("300x200")

# Labels e campos de entrada
label_user = tk.Label(root, text="Usuatio")
label_user.pack(pady=5)

entry_user = tk.Entry(root)
entry_user.pack(pady=5)

label_senha = tk.Label(root, text="Senha")
label_senha.pack(pady=5)

entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

# Botão de login
botao_login = tk.Button(root, text="Login", command=validar_login)
botao_login.pack(pady=10)

# Inicia a interface
root.mainloop()
