import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.utils.build_calendar import *
from assets.func.utils.sheet_info import *
from assets.func.utils.greeting_define import greeting_define
from assets.func.utils.process_name import process_name
from assets.func.utils.pop_up import show_popup, show_popup_bar

def define_dir(client):
    PROFILE_DIR = os.path.expanduser(f"~/.whatsapp_automation_profile_{client}")  # Altere conforme necessário
    return PROFILE_DIR
"""

PROFILE_DIR = os.path.expanduser(f"~/.whatsapp_automation_profile")  # Altere conforme necessário
    
"""
driver = None  # Inicializa o driver como None
number = ''
message = ''

def start_whatsapp(client):
    global driver
   
    stop_event = threading.Event()  # Criar o evento de parada
    popup, progress = show_popup_bar("Aguarde o WhatsApp abrir...", stop_event)

    def update_progress(start, end, step, delay=0.3):
        for value in range(start, end + 1, step):
            progress["value"] = value
            popup.update_idletasks()
            time.sleep(delay)

    try:
          
        if driver is None or not driver:
            
            options = webdriver.ChromeOptions() 
            options.page_load_strategy = 'eager'           
            options.add_argument("--headless")            
            options.add_argument(f"user-data-dir={define_dir(client)}")          
            driver = webdriver.Chrome(options=options)        
            driver.get("https://web.whatsapp.com")

            
            update_progress(0, 50, 1, 0.1)  
                              
            WebDriverWait(driver,2).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            
            update_progress(70, 90, 1, 0.1)  
           
            
    except Exception as e:
        
        popup.destroy()
        
        
        driver.quit()
        options = webdriver.ChromeOptions() 
        options.page_load_strategy = 'eager'
        options.add_argument(f"user-data-dir={define_dir(client)}")          
        driver = webdriver.Chrome(options=options)        
        driver.get("https://web.whatsapp.com")
        
        show_popup('Scaneie o QRCode e depois de logado\nclique em OK para prosseguir')
        
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        
        popup, progress = show_popup_bar("Carregando ...", stop_event)

        driver.quit()
          
        options = webdriver.ChromeOptions() 
        options.page_load_strategy = 'eager'           
        options.add_argument("--headless")            
        options.add_argument(f"user-data-dir={define_dir(client)}")          
        driver = webdriver.Chrome(options=options)        
        driver.get("https://web.whatsapp.com")

        update_progress(0, 50, 1, 0.2)    
                        
        WebDriverWait(driver,2).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
      
        update_progress(70, 90, 1, 0.2) 

    finally:
        update_progress(90, 100, 1 , 0.01)  # Finaliza o progresso
        popup.destroy()
        show_popup("WhatsApp pronto.")
    
    
def build_msg(page, message ): 
    global driver 
       
    if not driver:
        #print("WhatsApp Web não foi iniciado!")
       
        show_popup("WhatsApp Web não foi iniciado!")
        return
    if page == -1:
        #print('Escolha uma Pagina da planilha!')
        show_popup('Escolha uma Pagina da planilha!')
        return

    msg = message
    try:
        sheet = sheet_info(page)
    except:
        print('Erro ao ler planilha')
        show_popup('Erro ao ler planilha')

    try:
        for row in sheet.iter_rows(min_row=2):
               
            raw_number = row[0].value
            raw_name = row[1].value
            birthDay = row[2].value

            if not raw_number:  
                #if root:
                    #root.quit()  # Fecha a janela, se necessário
                break  # Sai do loop

            today = f"{current_day}-{current_month:02}"

            if today == birthDay:
                
                # Converte valores para string (se necessário)
                number = str(raw_number)
                name = str(process_name(raw_name))
                
                hour, minute = get_time()
                greeting = greeting_define(hour, name)

                message = f"{greeting} {msg}"
                
                
    except:
        print('Erro ao montar msg')
        show_popup('Erro ao montar msg')
        
    
    finally:
        try:    
                   
            # Busca pelo contato ou número
            search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            search_box.click()
            search_box.clear()
            search_box.send_keys(number + Keys.ENTER)
            time.sleep(2)  # Aguarda a tela do contato carregar

            # Digita e envia a message
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            msg_box.send_keys(message + Keys.ENTER)
            #print(f"Mensagem enviada para {name}")
            time.sleep(5)
            
        except Exception as e:
            print(f"Mensagem para: {name} NÃO FOI ENVIADA. Erro: {e}")
