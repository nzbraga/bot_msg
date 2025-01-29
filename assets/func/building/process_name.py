def process_name(full_name):
    # Remove espaços extras e divide o nome completo em partes
    parts = full_name.strip().split(" ")
    # Retorna o primeiro nome com a primeira letra maiúscula
    first_name = parts[0].capitalize() if parts else ''
    return first_name
