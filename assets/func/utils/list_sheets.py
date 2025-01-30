import openpyxl

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
        return []
    except Exception as e:
        print(f"Erro inesperado ao listar : {e}")
        return []


