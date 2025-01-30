from threading import Thread
from assets.func.utils.list_sheets import list_sheets



def refresh_page_sheets(dir, combobox):
    opcoes_pagina = list_sheets(dir + "/list_name.xlsx")
    combobox["values"] = opcoes_pagina
    combobox.set('Escolha a pagina')
