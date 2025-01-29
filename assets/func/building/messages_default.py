import random
import tkinter as tk
# Função para atualizar o campo de mensagem com base no combobox

def get_predefined_message(option):
    predefined_messages = {
        'Aniversario': [
            'Feliz aniversário! Que seu dia seja repleto de alegria e realizações!',
            'Parabéns pelo seu dia especial! Muitas bênçãos e felicidade!',
            'Que todos os seus sonhos se realizem neste aniversário!'
        ],        
        'Pascoa': [
            'Feliz Páscoa! Que a esperança e a renovação sejam constantes em sua vida.',
            'Que nesta Páscoa, a alegria e o amor encham seu coração.',
            'Celebre a Páscoa com paz e gratidão!'
        ],
        'Natal': [
            'Feliz Natal! Que a magia desta época ilumine sua vida.',
            'Desejamos um Natal cheio de amor, paz e alegria!',
            'Que o espírito natalino esteja presente em todos os momentos.'
        ],
        'Ano Novo': [
            'Feliz Ano Novo! Que este ano seja de conquistas e felicidade.',
            'Um novo ano está começando! Aproveite cada momento.',
            'Desejo a você um ano repleto de realizações e prosperidade!'
        ]
    }
    messages = predefined_messages.get(option, [])
    return random.choice(messages) if messages else ""
