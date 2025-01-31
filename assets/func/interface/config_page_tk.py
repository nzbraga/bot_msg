import tkinter as tk
from PIL import Image, ImageTk

def config_page_tk(lar, alt, root):
    logo = Image.open("logo_nzap.ico")    
    logo = logo.resize((30, 30))  
    logo_tk = ImageTk.PhotoImage(logo)   
    root.iconphoto(True, logo_tk)
    largura_janela = lar
    altura_janela = alt
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")