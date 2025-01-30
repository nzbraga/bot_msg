import openpyxl
from assets.func.utils.pop_up import *

def list_sheets(caminho_arquivo):
 
    try:
        # Abre a planilha em modo somente leitura
        workbook = openpyxl.load_workbook(caminho_arquivo, read_only=True)
                
        # Pega os nomes das sheets
        nomes_sheets = workbook.sheetnames      
        workbook.close()
       
      
        return nomes_sheets
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
        show_popup('Arquivo Excel nao encontrado\n1- Garanta que o arquivo esta no formato ".xlsl"\n2- O arquivo deve estar no mesmo lugar que o executavel!')
        return []
    except Exception as e:
        print(f"Erro inesperado ao listar : {e}")
        return []



