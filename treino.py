import json

def carregardados():
    try:
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvardados(dados):
    with open('usuarios.json', 'w') as file:
        json.dump(dados, file, indent=4)

def registrarusuario():
    nome = input('Digite seu nome: ').upper()
    email = input('Digite seu email: ').upper()
    idade = input('Digite sua idade: ')

    dados = carregardados()

    if email in dados:
        print('Usuário já registrado')
    else:
        dados[email] = {'nome': nome, 'idade': idade}
        salvardados(dados)
        print('Usuário registrado')

def listar():
    dados = carregardados()
    if not dados:
        print('Nenhum usuário registrado.')
    else:
        for email, info in dados.items():
            print(f'Email: {email}, Nome: {info["nome"]}, Idade: {info["idade"]}')

def excluir():
    email = input('Digite o email de quem você deseja excluir: ').upper
    dados = carregardados()

    if email in dados:
        del dados[email]
        salvardados(dados)
        print('Usuário excluído.')
    else:
        print('Usuário não encontrado.')

def menu():
    while True:
        print("\nMenu:")
        print("1. Registrar usuário")
        print("2. Listar usuários")
        print("3. Excluir usuário")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrarusuario()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            excluir()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
