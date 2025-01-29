
import tkinter as tk
from tkinter import ttk, messagebox
import threading

def show_popup( message):
   
    # Cria a janela principal
    root = tk.Tk()
    root.attributes("-topmost", True)
        
    # Definir o tamanho da janela
    largura_janela = 300
    altura_janela = 80

    # Obter o tamanho da tela
    largura_tela = 1920
    altura_tela = 1080

    # Calcular a posição central
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Definir a geometria centralizada

    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    root.withdraw()  # Esconde a janela principal (não será mostrada)
    
    # Exibe a caixa de mensagem com a mensagem desejada
    messagebox.showinfo("Atenção", message)
  
    
def show_popup_bar(message, stop_event):
    popup = tk.Toplevel()
    popup.title("Aguarde...")
    popup.attributes("-topmost", True)

    largura_janela = 300
    altura_janela = 100
    largura_tela = popup.winfo_screenwidth()
    altura_tela = popup.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    popup.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    popup.resizable(False, False)

    tk.Label(popup, text=message, wraplength=280).pack(pady=10)

    progress = ttk.Progressbar(popup, orient="horizontal", length=250, mode="determinate")
    progress.pack(pady=10)

    return popup, progress

