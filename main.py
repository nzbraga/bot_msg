import os
import sys
import tkinter as tk
from tkinter import ttk
from threading import Thread

from assets.func.building.build_msg import *
from assets.func.utils.list_sheets import list_sheets

client = False
# Verifica se o argumento 'client' foi passado
if len(sys.argv) > 1 :
    client = sys.argv[1]   
else:
    print('erro cliente')

# Funções do programa
# Funções do programa
def start_whatsapp_thread(client):
    """Inicia a thread do WhatsApp com o client passado"""
    thread = Thread(target=start_whatsapp, args=(client,))
    thread.start()

def send_message(page):   
    message = message_entry.get("1.0", tk.END).strip()
    build_msg(page, message)

def atualizar_paginas():
    opcoes_pagina = list_sheets(diretorio_raiz + "/list_name.xlsx")
    combobox_pagina["values"] = opcoes_pagina
    combobox_pagina.set('Escolha a pagina')

# Diretório raiz
diretorio_raiz = os.getcwd()

root = tk.Tk()
root.title("nZap autoSend")

largura_janela = 400
altura_janela = 300
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

frame_pagina = tk.Frame(root)
frame_pagina.pack(pady=5)

label_pagina = tk.Label(frame_pagina, text="Pagina:")
label_pagina.pack(side=tk.LEFT, padx=5)

opcoes_pagina = list_sheets(diretorio_raiz + "/list_name.xlsx")
combobox_pagina = ttk.Combobox(frame_pagina, values=opcoes_pagina, state="readonly")
combobox_pagina.set('Escolha a pagina')
combobox_pagina.pack(side=tk.LEFT, padx=5)

botao_atualizar = tk.Button(frame_pagina, text="⟳", command=atualizar_paginas, width=3, height=1)
botao_atualizar.pack(side=tk.LEFT, padx=5)

message_label = tk.Label(root, text="Mensagem:")
message_label.pack(pady=5)

message_entry = tk.Text(root, width=40, height=5)
message_entry.pack(pady=5)

send_button = tk.Button(root, text="Enviar", command=lambda: send_message(combobox_pagina.current()))
send_button.pack(pady=10)

status_label = tk.Label(root, text="Aguardando conexão com WhatsApp\n Se necessário escaneie o QR Code", fg="green")
status_label.pack(pady=10)

# Se 'client' foi passado, inicializa o WhatsApp
if client:
    start_whatsapp_thread(client)
else:
    start_whatsapp_thread('braga')

root.mainloop()
