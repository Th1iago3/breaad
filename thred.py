import os
import requests
from pyfiglet import figlet_format
from colorama import Fore, Back, Style, init
import time
import random
import string

# Limpar a tela
os.system("clear" if os.name == "posix" else "cls")

# Inicializar colorama
init(autoreset=True)

# Variáveis globais
credenciais_exibidas = False
cu = None

# Função para gerar strings aleatórias
def random_string(length, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))

# Função para gerar um email aleatório
def gerar_email_aleatorio():
    nome = random_string(5)
    numero = random.randint(100, 999)
    dominio = ['gmail.com', 'yahoo.com', 'outlook.com']
    return f"{nome}{numero}@{random.choice(dominio)}"

# Função para cadastrar o usuário automaticamente
def cadastrar_usuario():
    global cu
    nome_usuario = random_string(8)
    email = gerar_email_aleatorio()
    senha = random_string(12, string.ascii_letters + string.digits + string.punctuation)

    # Enviar o cadastro
    response = requests.post(
        "https://yuukiapis.site/cadastrar",
        json={"nome": nome_usuario, "email": email, "senha": senha}
    )
    
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            print(Fore.GREEN + Style.BRIGHT + f"[ THREAD ]: Conta criada com sucesso! Usuário: {nome_usuario}, Email: {email}")
            cu = nome_usuario
        else:
            print(Fore.RED + Style.BRIGHT + f"[ THREAD ]: Erro ao criar conta: {data.get('mensagem', 'Desconhecido')}")
    else:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Erro na solicitação de cadastro.")

# Função para exibir credenciais
def cred():
    global cu
    try:
        re = requests.get("https://yuukiapis.site/meus-dados")
        rej = re.json()
        cu = rej["nome"]
        print(Fore.BLUE + Style.BRIGHT + f"[ THREAD ]: Bem-vindo(a), {cu}.")
    except KeyError:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Não foi possível pegar as credenciais.")
        print(Fore.YELLOW + Style.BRIGHT + "[ THREAD ]: Gerando conta automaticamente...")
        cadastrar_usuario()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"[ THREAD ]: Erro ao conectar ao servidor: {e}")

# Função para exibir o logo
def mostrar_logo():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color = random.choice(colors)
    print(color + Style.BRIGHT + figlet_format("Thread", font="slant"))

# Função para exibir a barra de separação
def separador():
    print(Fore.YELLOW + Style.BRIGHT + "=" * 50)

# Menu principal
def mostrar_menu():
    time.sleep(2)
    global credenciais_exibidas
    
    if not credenciais_exibidas:
        print(Fore.GREEN + Style.BRIGHT + f"[ THREAD ]: Credenciais Encontradas com sucesso!")
        time.sleep(4)
        cred()
        separador()
        credenciais_exibidas = True
        
    print(Fore.YELLOW + Style.BRIGHT + "[ THREAD ]: Menu Principal")
    separador()
    print(Fore.CYAN + Style.BRIGHT + "[1] Adicionar Plano")
    print(Fore.CYAN + Style.BRIGHT + "[2] Atualizar Token")
    print(Fore.CYAN + Style.BRIGHT + "[3] Atualizar IP")
    print(Fore.CYAN + Style.BRIGHT + "[4] Enviar Aviso")
    print(Fore.CYAN + Style.BRIGHT + "[5] Adicionar Administrador")
    print(Fore.CYAN + Style.BRIGHT + "[6] Remover Administrador")
    print(Fore.CYAN + Style.BRIGHT + "[7] Mostrar Usuários")
    print(Fore.CYAN + Style.BRIGHT + "[8] Banir Usuário")
    print(Fore.CYAN + Style.BRIGHT + "[9] Desbanir Usuário")
    print(Fore.CYAN + Style.BRIGHT + "[10] Sair")
    separador()
    return input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Escolha uma opção: ")

# Função para adicionar plano
def adicionar_plano():
    separador()
    nome = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Nome do usuário: ")
    dias = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Dias: ")
    response = requests.post(
        "https://yuukiapis.site/adicionar-plano",
        headers={"Authorization": "Bearer paocomovo"},
        json={"nome": nome, "dias": int(dias), "plano": "premium"}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")

# Função para atualizar token
def atualizar_token():
    separador()
    nome = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Nome do usuário: ")
    token = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Token: ")
    response = requests.post(
        "https://yuukiapis.site/atualizar-token",
        headers={"Authorization": "Bearer paocomovo"},
        json={"nome": nome, "token": token}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")

# Função para atualizar IP
def atualizar_ip():
    separador()
    nome = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Nome do usuário: ")
    ip = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: IP: ")
    response = requests.post(
        "https://yuukiapis.site/atualizar-ipp",
        headers={"Authorization": "Bearer paocomovo"},
        json={"nome": nome, "ip": ip}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")

# Função para enviar aviso
def enviar_aviso():
    separador()
    aviso = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Aviso a ser enviado: ")
    response = requests.post(
        "https://yuukiapis.site/enviar-aviso",
        headers={"Authorization": "Bearer paocomovo"},
        json={"aviso": aviso}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")

# Função para exibir usuários
def mostrar_usuarios():
    separador()
    response = requests.get(
        "https://yuukiapis.site/usuarios",
        headers={"Authorization": "Bearer paocomovo"}
    )
    usuarios = response.json()
    print(Fore.YELLOW + Style.BRIGHT + "[ THREAD ]: Lista de Usuários:")
    separador()
    for usuario in usuarios:
        plano = f" | Plano: {usuario.get('plano', 'Não especificado')}"
        print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {usuario['nome']} ✅\n| {usuario['senha']}\n| {usuario['token']} \n| {usuario['ip']}\n=========================\n")
    separador()

# Função para adicionar administrador
def adicionar_adm():
    separador()
    response = requests.get(
        "https://yuukiapis.site/usuarios",
        headers={"Authorization": "Bearer paocomovo"}
    )
    usuarios = response.json()

    print(Fore.YELLOW + Style.BRIGHT + "[ THREAD ]: Lista de Usuários sem Admin:")
    separador()
    usuarios_sem_admin = [u for u in usuarios if not u.get("admin", False)]
    
    if not usuarios_sem_admin:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Não há usuários para adicionar como administrador.")
        separador()
        return

    for usuario in usuarios_sem_admin:
        print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {usuario['nome']}")

    nome_usuario = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Digite o nome do usuário para adicionar como administrador: ")
    usuario_encontrado = next((u for u in usuarios if u['nome'] == nome_usuario), None)

    if usuario_encontrado:
        response = requests.post(
            "https://yuukiapis.site/usuarios/acao",
            headers={"Authorization": "Bearer paocomovo"},
            json={"acao": "AddAdmUsuario", "nome": nome_usuario, "quantidade": 1}
        )
        print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: ✅ Sucesso! {nome_usuario} is_admin=true")
    else:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Usuário não encontrado.")
    separador()

# Função para remover administrador
def remover_adm():
    separador()
    response = requests.get(
        "https://yuukiapis.site/usuarios",
        headers={"Authorization": "Bearer paocomovo"}
    )
    usuarios = response.json()

    print(Fore.YELLOW + Style.BRIGHT + "[ THREAD ]: Lista de Administradores:")
    separador()
    usuarios_com_admin = [u for u in usuarios if u.get("admin", False)]
    
    if not usuarios_com_admin:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Não há administradores para remover.")
        separador()
        return

    for usuario in usuarios_com_admin:
        print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {usuario['nome']}")

    nome_usuario = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Digite o nome do administrador para remover: ")
    usuario_encontrado = next((u for u in usuarios if u['nome'] == nome_usuario), None)

    if usuario_encontrado:
        response = requests.post(
            "https://yuukiapis.site/usuarios/acao",
            headers={"Authorization": "Bearer paocomovo"},
            json={"acao": "RemoverAdmUsuario", "nome": nome_usuario, "quantidade": 0}
        )
        print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: ✅ Sucesso! {nome_usuario} is_admin=false")
    else:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Usuário não encontrado.")
    separador()

# Função para banir usuário
def banir_usuario():
    separador()
    nome_usuario = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Digite o nome do usuário para banir: ")
    response = requests.post(
        "https://yuukiapis.site/usuarios/acao",
        headers={"Authorization": "Bearer paocomovo"},
        json={"acao": "banirUsuario", "nome": nome_usuario, "quantidade": 0}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")
    separador()

# Função para desbanir usuário
def desbanir_usuario():
    separador()
    nome_usuario = input(Fore.WHITE + Style.BRIGHT + "[ THREAD ]: Digite o nome do usuário para desbanir: ")
    response = requests.post(
        "https://yuukiapis.site/usuarios/acao",
        headers={"Authorization": "Bearer paocomovo"},
        json={"acao": "desbanirUsuario", "nome": nome_usuario, "quantidade": 0}
    )
    print(Fore.YELLOW + Style.BRIGHT + f"[ THREAD ]: {response.text}")
    separador()

# Função de Easter Egg
def opfun_easteregg(comando):
    if cu is None:
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Erro: Credenciais não definidas. Por favor, recarregue o programa.")
        return

    if comando == "b":
        print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Banindo todos os usuários...")
        time.sleep(2)
        response = requests.get(
            "https://yuukiapis.site/usuarios",
            headers={"Authorization": "Bearer paocomovo"}
        )
        usuarios = response.json()
        for usuario in usuarios:
            if usuario['nome'] != cu:
                requests.post(
                    "https://yuukiapis.site/usuarios/acao",
                    headers={"Authorization": "Bearer paocomovo"},
                    json={"acao": "banirUsuario", "nome": usuario['nome'], "quantidade": 0}
                )
                print(Fore.RED + Style.BRIGHT + f"[ THREAD ]: {usuario['nome']} banido.")
                time.sleep(0.5)
        print(Fore.GREEN + Style.BRIGHT + "[ THREAD ]: ✅ ! Todos os usuários foram banidos...")
    elif comando == "d":
        print(Fore.GREEN + Style.BRIGHT + "[ THREAD ]: Desbanindo todos os usuários...")
        time.sleep(2)
        response = requests.get(
            "https://yuukiapis.site/usuarios",
            headers={"Authorization": "Bearer paocomovo"}
        )
        usuarios = response.json()
        for usuario in usuarios:
            if usuario['nome'] != cu:
                requests.post(
                    "https://yuukiapis.site/usuarios/acao",
                    headers={"Authorization": "Bearer paocomovo"},
                    json={"acao": "desbanirUsuario", "nome": usuario['nome'], "quantidade": 0}
                )
                print(Fore.GREEN + Style.BRIGHT + f"[ THREAD ]: {usuario['nome']} desbanido.")
                time.sleep(0.5)
        print(Fore.GREEN + Style.BRIGHT + "[ THREAD ]: ✅ ! Todos os usuários foram desbanidos.")

# Função principal
def main():
    mostrar_logo()

    while True:
        escolha = mostrar_menu()
        mostrar_logo()  # Mostra o logo novamente após a escolha de menu
        
        if escolha.startswith("/opfun "):
            comando = escolha.split()[1]
            opfun_easteregg(comando)
        elif escolha == "1":
            adicionar_plano()
        elif escolha == "2":
            atualizar_token()
        elif escolha == "3":
            atualizar_ip()
        elif escolha == "4":
            enviar_aviso()
        elif escolha == "5":
            adicionar_adm()
        elif escolha == "6":
            remover_adm()
        elif escolha == "7":
            mostrar_usuarios()
        elif escolha == "8":
            banir_usuario()
        elif escolha == "9":
            desbanir_usuario()
        elif escolha == "10":
            print(Fore.GREEN + Style.BRIGHT + "[ THREAD ]: Saindo...")
            break
        else:
            print(Fore.RED + Style.BRIGHT + "[ THREAD ]: Opção inválida. Tente novamente.")

# Executando o script
if __name__ == "__main__":
    main()
