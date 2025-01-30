import os
import tkinter as tk
from tkinter import ttk
from assets.func.utils.list_sheets import list_sheets
from assets.func.interface.start_whatsapp_thread import start_whatsapp_thread
from assets.func.interface.send_message import send_message
from assets.func.interface.refresh_page_sheets import refresh_page_sheets

def send_screen(client):
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

    diretorio_raiz = os.getcwd()
    opcoes_pagina = list_sheets(diretorio_raiz + "/list_name.xlsx")
    combobox_pagina = ttk.Combobox(frame_pagina, values=opcoes_pagina, state="readonly")
    combobox_pagina.set('Escolha a pagina')
    combobox_pagina.pack(side=tk.LEFT, padx=5)

    botao_atualizar = tk.Button(frame_pagina, text="⟳", command=lambda: refresh_page_sheets(diretorio_raiz, combobox_pagina), width=3, height=1)
    botao_atualizar.pack(side=tk.LEFT, padx=5)

    message_label = tk.Label(root, text="Mensagem:")
    message_label.pack(pady=5)

    message_entry_send = tk.Text(root, width=40, height=5)
    message_entry_send.pack(pady=5)

    send_button = tk.Button(root, text="Enviar", command=lambda: send_message(combobox_pagina.current(), message_entry_send.get("1.0", tk.END).strip()))
    send_button.pack(pady=10)

    status_label = tk.Label(root, text="Aguardando conexão com WhatsApp\n Se necessário escaneie o QR Code", fg="green")
    status_label.pack(pady=10)

    start_whatsapp_thread(client)
    root.mainloop()
