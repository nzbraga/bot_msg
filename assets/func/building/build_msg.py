import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.building.build_calendar import *
from assets.func.building.sheet_info import *
from assets.func.building.greeting_define import greeting_define
from assets.func.building.process_name import process_name
from assets.func.utils.pop_up import show_popup, show_popup_bar


# Diretório para armazenar o perfil do Chrome
PROFILE_DIR = os.path.expanduser("~/.whatsapp_automation_profile")  # Altere conforme necessário
driver = None  # Inicializa o driver como None

def build_msg( message , root=None):  
    
    
    if not driver:
        #print("WhatsApp Web não foi iniciado!")
        show_popup("WhatsApp Web não foi iniciado!")
        return

    msg = message

    sheet = sheet_info()

    for row in sheet.iter_rows(min_row=2):
        number = row[0].value
        raw_name = row[1].value
        birthDay = row[2].value

        # Verifica se o número é vazio ou None
        if not number:  
            if root:
                #root.quit()  # Fecha a janela, se necessário
                break  # Sai do loop
        
        # Converte valores para string (se necessário)
        number = str(number)
        name = str(process_name(raw_name))
        
        hour, minute = get_time()
        greeting = greeting_define(hour, name)

        mensagem = f"{greeting} {msg}"
        today = f"{current_day}-{current_month:02}"
        
        if today == birthDay:
       
            try:    
            
                # Busca pelo contato ou número
                search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
                search_box.click()
                search_box.clear()
                search_box.send_keys(number + Keys.ENTER)
                time.sleep(2)  # Aguarda a tela do contato carregar

                # Digita e envia a mensagem
                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                msg_box.click()
                msg_box.send_keys(mensagem + Keys.ENTER)
                print(f"Mensagem enviada para {name}")
                time.sleep(5)
                
            except Exception as e:
                print(f"Mensagem para: {name} NÃO FOI ENVIADA. Erro: {e}")

def start_whatsapp():
    global driver

    stop_event = threading.Event()  # Criar o evento de parada
    popup, progress = show_popup_bar("Aguarde o WhatsApp abrir...", stop_event)

    def update_progress(value):
        progress["value"] = value
        popup.update_idletasks()

    try:
          
        if driver is None or not driver:
            update_progress(5)  
            options = webdriver.ChromeOptions()            
            options.add_argument("--headless")            
            options.add_argument(f"user-data-dir={PROFILE_DIR}")          
            driver = webdriver.Chrome(options=options)        
            driver.get("https://web.whatsapp.com")
            update_progress(10)  
            time.sleep(0.5)
            update_progress(15)  
            time.sleep(0.5)          
            update_progress(20)  
            time.sleep(0.5)          
            update_progress(26)  
            time.sleep(0.5)
            update_progress(28)  
            time.sleep(0.5)          
            update_progress(30)  
            time.sleep(0.5)          
            update_progress(32)                   
            time.sleep(0.3)          
            update_progress(34)  
            time.sleep(0.3)
            update_progress(36)  
            time.sleep(0.3)          
            update_progress(38)  
            time.sleep(0.3)          
            update_progress(40)  
            time.sleep(0.3)
            update_progress(42)  
            time.sleep(0.3)          
            update_progress(44)  
            time.sleep(0.3)          
            update_progress(46)                   
            time.sleep(0.3)          
            update_progress(48)                   
            time.sleep(0.3)          
            update_progress(50)                   
            WebDriverWait(driver,2).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            update_progress(70)  
            time.sleep(0.3)
            update_progress(75)  
            time.sleep(0.3)
            update_progress(80)  
            time.sleep(0.3)
            update_progress(90) 
            
    except Exception as e:
        popup.destroy()
        
        driver.quit()
        options = webdriver.ChromeOptions() 
        options.add_argument(f"user-data-dir={PROFILE_DIR}")          
        driver = webdriver.Chrome(options=options)        
        driver.get("https://web.whatsapp.com")
        
        show_popup('Scaneie o QRCode...\n depois de logado clique em OK para prosseguir')
        
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        
        popup, progress = show_popup_bar("Carregando ...", stop_event)

        driver.quit()
        update_progress(5)  
        options = webdriver.ChromeOptions()            
        options.add_argument("--headless")            
        options.add_argument(f"user-data-dir={PROFILE_DIR}")          
        driver = webdriver.Chrome(options=options)        
        driver.get("https://web.whatsapp.com")
        update_progress(10)  
        time.sleep(0.5)   
        update_progress(20)  
        time.sleep(0.5)   
        update_progress(30)  
        time.sleep(0.5)  
        update_progress(40)  
        time.sleep(0.3)
        update_progress(42)  
        time.sleep(0.3)          
        update_progress(44)  
        time.sleep(0.3)          
        update_progress(46)                   
        time.sleep(0.3)          
        update_progress(48)                   
        time.sleep(0.3)          
        update_progress(50)                   
        WebDriverWait(driver,2).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        update_progress(70)  
        time.sleep(0.3)
        update_progress(75)  
        time.sleep(0.3)
        update_progress(80)  
        time.sleep(0.3)
        update_progress(90)   

    finally:
        update_progress(100)  # Finaliza o progresso
        popup.destroy()
        show_popup("WhatsApp pronto.")