import schedule
import time
import datetime
import threading
from assets.func.utils.pop_up import show_popup
from assets.func.building.build_msg import build_msg

def schedule_msg(day, hour, page, message):
    """Agenda o envio de mensagens conforme a frequência especificada."""

    if day == "Quinzenal":
        print(f"Envio agendado para cada 15 dias às {hour}!")
        show_popup(f"Envio agendado para cada 15 dias às {hour}!")
        schedule.every(15).days.at(hour).do(lambda: build_msg(page, message))

    elif day == "Semanal":
        today = datetime.datetime.today()
        weekday = today.weekday()  # 0 = Segunda, 6 = Domingo
        print(f"Envio agendado para toda {today.strftime('%A')} às {hour}!")
        show_popup(f"Envio agendado para toda {today.strftime('%A')} às {hour}!")
        schedule.every().week.at(hour).do(lambda: executar_no_dia(weekday, page, message, weekly=True))

    else:
        if day == "Diário":
            print(f"Envio agendado para todos os dias às {hour}!")
            show_popup(f"Envio agendado para todos os dias às {hour}!")
        else:
            print(f"Envio agendado para todo dia {day} às {hour}!")
            show_popup(f"Envio agendado para todo dia {day} às {hour}!")

        schedule.every().day.at(hour).do(lambda: executar_no_dia(day, page, message))

def executar_no_dia(day, page, message, weekly=False):
    """Executa a mensagem no dia correto, seja diariamente ou semanalmente."""

    today = datetime.datetime.today()

    if weekly:
        if today.weekday() == day:  # 0 = Segunda, 6 = Domingo
            build_msg(page, message)
            print(f"Mensagem enviada no dia {today.strftime('%A')} ({today.strftime('%d/%m/%Y')}) às {today.strftime('%H:%M:%S')}!")
    else:
        if day == "Diário" or today.day == int(day):
            build_msg(page, message)
            print(f"Mensagem enviada no dia {today.day} às {today.strftime('%H:%M:%S')}!")

def run_scheduler():
    """Executa o loop de agendamento em uma thread separada."""
    while True:
        schedule.run_pending()
        time.sleep(30)  # Verifica as tarefas pendentes a cada 30 segundos

# Inicia o loop do schedule em uma thread separada
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()
