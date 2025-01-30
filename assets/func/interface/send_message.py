from assets.func.building.build_msg import build_msg

def send_message(page, message_entry):   
    message = message_entry
    build_msg(page, message)
