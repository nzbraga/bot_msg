import json
import uuid
import os

USUARIOS_FILE = ".usuarios.json"
SESSAO_FILE = ".sessao.json"

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON."""
    if os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    """Salva os usuários no arquivo JSON."""
    with open(USUARIOS_FILE, "w") as f:
        json.dump(usuarios, f, indent=4)

def carregar_sessao():
    """Carrega o usuário logado do arquivo JSON."""
    if os.path.exists(SESSAO_FILE):
        with open(SESSAO_FILE, "r") as f:
            return json.load(f).get("user_name")
    return None

def salvar_sessao(usuario_id, name):
    """Salva o usuário logado no arquivo JSON."""
    with open(SESSAO_FILE, "w") as f:
        json.dump({"user_id": usuario_id, "user_name": name }, f)

def autenticar_usuario(nome):
    """Verifica se o usuário já existe ou cria um novo."""
    usuarios = carregar_usuarios()

    # Verifica se o nome já existe
    for user_id, user_name in usuarios.items():
        if user_name.lower() == nome.lower():
            salvar_sessao(user_id, user_name)
            return user_name.upper()

    # Criar novo usuário com ID único
    novo_id = str(uuid.uuid4())
    usuarios[novo_id] = nome
    salvar_usuarios(usuarios)
    salvar_sessao(novo_id, user_name)
    return nome.upper()

def logout():
    """Remove a sessão salva (desloga o usuário)."""
    if os.path.exists(SESSAO_FILE):
        os.remove(SESSAO_FILE)