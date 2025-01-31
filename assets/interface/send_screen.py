import os
import tkinter as tk
from tkinter import ttk
from assets.func.utils.list_sheets import list_sheets
from assets.func.interface.start_whatsapp_thread import start_whatsapp_thread
from assets.func.interface.send_message import send_message
from assets.func.interface.refresh_page_sheets import refresh_page_sheets
from assets.interface.utils.back_login import back_login
from assets.func.login.registration_users import logout
from assets.func.interface.config_page_tk import config_page_tk
from assets.func.utils.schedule import schedule_msg

def open_main_app(client):
    """Cria a interface principal do aplicativo."""
    
    root = tk.Tk()
    root.title(f"nZap autoSend - {client}")

    config_page_tk(400, 350, root)

    frame_pagina = tk.Frame(root)
    frame_pagina.pack(pady=5)

    label_pagina = tk.Label(frame_pagina, text="Página:")
    label_pagina.pack(side=tk.LEFT, padx=10)

    diretorio_raiz = os.getcwd()
    opcoes_pagina = list_sheets(diretorio_raiz + "/list_name.xlsx")
    combobox_pagina = ttk.Combobox(frame_pagina, values=opcoes_pagina, state="readonly")
    combobox_pagina.set('Escolha a página')
    combobox_pagina.pack(side=tk.LEFT, padx=5)

    botao_atualizar = tk.Button(frame_pagina, text="⟳", command=lambda: refresh_page_sheets(diretorio_raiz, combobox_pagina), width=3, height=1)
    botao_atualizar.pack(side=tk.LEFT, padx=5)

    message_label = tk.Label(root, text="Mensagem:")
    message_label.pack(pady=5)

    message_entry_send = tk.Text(root, width=40, height=5)
    message_entry_send.pack(pady=0)

    frame = tk.Frame(root)
    frame.pack(padx=5, pady=10)

    # Lista de dias
    custom_options = ["Diário", "Semanal", "Quinzenal"]
    days = [f"{d:02}" for d in range(1, 32)]
    all_options = custom_options + days

    combobox_days = ttk.Combobox(frame, values=all_options, width=10)
    combobox_days.set('Diário')
    combobox_days.pack(side="left", padx=5, pady=2)

    # Lista de horas
    hours = [f"{h:02}:00" for h in range(8, 19)]
    combobox_hours = ttk.Combobox(frame, values=hours, width=5)
    combobox_hours.set('08:00')
    combobox_hours.pack(side="left", padx=5, pady=2)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=0)

    # Botão "Agendar"
    schedule_button = tk.Button(
        button_frame, 
        text="Agendar", 
        command=lambda: schedule_msg(
            combobox_days.get(), 
            combobox_hours.get(), 
            combobox_pagina.current(),
            message_entry_send.get("1.0", tk.END).strip()
        )
    )
    schedule_button.pack(side="left", padx=5, pady=0) 

    # Botão "Enviar Agora"
    send_button = tk.Button(
        button_frame, 
        text="Enviar Agora", 
        command=lambda: send_message(
            combobox_pagina.current(),
            message_entry_send.get("1.0", tk.END).strip()
        )
    )
    send_button.pack(side="left", padx=5, pady=0)

    status_label = tk.Label(root, text="Aguardando conexão com WhatsApp\nSe necessário, escaneie o QR Code", fg="green")
    status_label.pack(pady=10)

    button_frame_exit = tk.Frame(root)
    button_frame_exit.pack(pady=0)

    back_button = tk.Button(button_frame_exit, text="Mudar Cliente", command=lambda: back_login(root))
    back_button.pack(side="left", padx=5, pady=0)

    disconnect_button = tk.Button(button_frame_exit, text="Desconectar", command=lambda: logout(), bg='red')
    disconnect_button.pack(side="left", padx=5, pady=0)

    start_whatsapp_thread(client)

    root.mainloop()
