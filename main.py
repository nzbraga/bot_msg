import tkinter as tk
from tkinter import ttk
from threading import Thread
from assets.func.building.build_msg import  *
from assets.func.utils.list_sheets import list_sheets

from assets.func.building.messages_default import get_predefined_message

diretorio_raiz = os.getcwd()

# Função para iniciar o WhatsApp Web em um thread separado
def start_whatsapp_thread():
    thread = Thread(target=start_whatsapp)
    thread.start()

# Função para enviar a mensagem com o valor da entrada de texto
def send_message(page):   
    message = message_entry.get("1.0", tk.END).strip()  # Obtém o texto da entrada
    build_msg(page, message)
"""
# Função para atualizar o campo de mensagem com base no combobox
def update_message(*args):
    selected_option = combobox_entry.get()
    message = get_predefined_message(selected_option)  # Obtém a mensagem do arquivo messages.py
    message_entry.delete("1.0", tk.END)  # Limpa o campo de texto
    message_entry.insert("1.0", message)  # Insere o texto correspondente
"""
# Criar a janela principal
root = tk.Tk()
root.title("Escala de Ministérios")

# Definir o tamanho da janela
largura_janela = 400
altura_janela = 300

# Obter o tamanho da tela
largura_tela = 1920
altura_tela = 1080

# Calcular a posição central
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Definir a geometria centralizada

root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

"""
# Combobox de msg padrão
combobox_label = tk.Label(root, text="Escolha um tema:")
combobox_label.pack(pady=5)

options = ['Aniversario','Pascoa', 'Natal', 'Ano Novo']
combobox_entry = ttk.Combobox(root, values=options)
combobox_entry.pack(pady=5)
combobox_entry.bind("<<ComboboxSelected>>", update_message)
"""
# Combobox "Pagina"
label_pagina = tk.Label(root, text="Pagina:")
label_pagina.pack( padx=5)

opcoes_pagina = list_sheets(diretorio_raiz + "/list_name.xlsx")
combobox_pagina = ttk.Combobox(root, values=opcoes_pagina, state="readonly")
combobox_pagina.set('Escolha a pagina')
combobox_pagina.pack( padx=5)


# Campo de entrada de texto para a mensagem
message_label = tk.Label(root, text="Mensagem:")
message_label.pack(pady=5)

message_entry = tk.Text(root, width=40, height=5)
message_entry.pack(pady=5)

# Botão para enviar as mensagens
send_button = tk.Button(root, text="Enviar", command=lambda: send_message(combobox_pagina.current()))
send_button.pack(pady=10)

# Label de status
status_label = tk.Label(root, text="Aguardando conexão com WhatsApp\n Se nescessario escaneie o QR Code", fg="green")
status_label.pack(pady=10)

# Inicia o WhatsApp Web no thread separado
start_whatsapp_thread()

# Iniciar o loop da interface
root.mainloop()
