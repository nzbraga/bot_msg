import tkinter as tk
from tkinter import ttk

def contact_list():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Agenda de Contatos")
    root.geometry("400x300")

    # Criar os campos de entrada
    frame_inputs = tk.Frame(root)
    frame_inputs.pack(pady=10)

    def adicionar_contato():
        nome = entry_nome.get()
        contato = entry_contato.get()
        ativo = var_ativo.get()
        if nome and contato:
            tree.insert("", "end", values=(nome, contato, "Sim" if ativo else "Não"))
            entry_nome.delete(0, tk.END)
            entry_contato.delete(0, tk.END)
            var_ativo.set(False)

    def remover_contato():
        selecionado = tree.selection()
        for item in selecionado:
            tree.delete(item)
    # Nome
    lbl_nome = tk.Label(frame_inputs, text="Nome:")
    lbl_nome.grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(frame_inputs)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    # Contato
    lbl_contato = tk.Label(frame_inputs, text="Contato:")
    lbl_contato.grid(row=1, column=0, padx=5, pady=5)
    entry_contato = tk.Entry(frame_inputs)
    entry_contato.grid(row=1, column=1, padx=5, pady=5)

    # Ativo
    var_ativo = tk.BooleanVar()
    chk_ativo = tk.Checkbutton(frame_inputs, text="Ativo", variable=var_ativo)
    chk_ativo.grid(row=2, columnspan=2, pady=5)

    # Botões
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=5)

    btn_adicionar = tk.Button(frame_buttons, text="Adicionar", command=adicionar_contato)
    btn_adicionar.pack(side=tk.LEFT, padx=5)

    btn_remover = tk.Button(frame_buttons, text="Remover", command=remover_contato)
    btn_remover.pack(side=tk.LEFT, padx=5)

    # Lista de contatos
    columns = ("Nome", "Contato", "Ativo")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.pack(pady=10)

    # Rodar a aplicação
    root.mainloop()
