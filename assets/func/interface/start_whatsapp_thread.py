from threading import Thread
from assets.func.building.build_msg import *

def start_whatsapp_thread(client):
    """Inicia a thread do WhatsApp com o client passado"""
    thread = Thread(target=start_whatsapp, args=(client,))
    thread.start()
