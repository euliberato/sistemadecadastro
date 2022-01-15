clientes = []
endereco = []

def cadastro():

    while True: 
        print('[Forneça as informações do usuário!]')

        dados = {} #Dicionário que será passado com todos os dados para a lista 'clientes'.
        dados['nomeComp'] = (input('Nome: '))
        dados['senha'] = input('Senha: ')

        #1) Endereço de e-mail:
        dados['email'] = input('E-mail: ')
        lista = {i['email']: i for i in clientes} #Variavel usada com indice e laço 'for': verifica repetições por meio das chaves.
        while dados['email'] in lista: #Caso o dado já esteja em uso, o programa solicita um dado diferente.
            dados['email'] = input('[E-mail em uso, tente novamente!] E-mail: ')

        #2) Login de usuário:
        dados['login'] = input('Login: ')
        lista = {i['login']: i for i in clientes}
        while dados['login'] in lista:
            dados['login'] = input('[Login em uso, tente novamente!] Login: ')

        #3) Telefone de usuário:
        dados['telefone'] = int(input('Telefone: '))
        lista = {i['telefone']: i for i in clientes}
        while dados['telefone'] in lista:
            dados['telefone'] = int(input('[Telefone em uso, tente novamente!] Telefone: '))

        clientes.append(dados) #Metodo 'append' irá adicionar os dados na lista.

        print('[OK! Cadastro concluído.]')
        opcao = input('Deseja cadastrar mais alguém? (S/N): ').strip().lower()
        if(opcao == 'n'): #Caso o administrador não queira novos usuários o laço 'while True' se encerra.
            menu()
            break

def cadEndereco():
    
    while True:
        
        print('[Forneça um login de usuário!]')
        lista = {i['login']: i for i in clientes}
        pesq = input('Login: ') 

        #Endereço só será cadastrado a um usuário válido

        if pesq in lista:
            print('[Forneça o endereço do cliente: ]')
            
            destino = {} #Dicionário contendo apenas informações de endereço do cliente.
            destino['id'] = pesq
            destino['estado'] = input('Estado: ')
            destino['cidade'] = input('Cidade: ')
            destino['rua'] = input('Rua e Número: ')
            destino['cep'] = input('CEP: ')
            endereco.append(destino) #Será armazenado em outra lista.

        else: 
            print('')
            print('[Usuário não encontrado!]')
            print('')

        opcao = input('Deseja cadastrar outro endereço? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarDados():

    while True:
        print('[Forneça o LOGIN para consultar os dados de um usuário!]')

        lista = {i['login']: i for i in clientes}
        lista2 = {i['id']: i for i in endereco}

        #Agora, teremos dois casos onde o cliente pode ou não estar com o endereço cadastrado (obs: o mesmo login deverá estar contido em ambas as listas: de clientes e de endereços.)

        pesq = input('Login: ')

        if pesq in lista and pesq not in lista2:

            print(f'Dados do cliente [{pesq.upper()}]: {lista[pesq]}') #Eventualmente o input 'pesq' estará na lista e caso seja 'True' através do operador 'in', irá retornar os dados do usuário.
            print('')
            print('[Endereço não cadastrado!]')
            print('')

        elif pesq in lista and pesq in lista2:

            print('')
            print(f'Dados do cliente [{pesq.upper()}]: {lista[pesq]}')
            print('')
            print(f'Endereços do cliente [{pesq.upper()}]:')
            print('')
            resultado = list(filter(lambda item: item['id'] == pesq, endereco)) #Filter com a função lambda irá filtrar os resultados a partir de uma chave específica dentro de uma lista com dicionários.
            for i in resultado:
                print(i)
            print('')
            
        else: 
            print('')
            print('[Usuário não encontrado!]')
            print('')

        opcao = input('Deseja consultar outro cliente? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarClientes():

    while True:
        print('')
        print('[Usuários Cadastrados: ]')
        print('')

        for i in clientes: #Variavel 'i' passa na lista 'clientes' buscando apenas as informações com indice 'login' e 'nomeComp', logo após retornando o output dos dados.

            print('Nome:', i['nomeComp'], 'Login:', i['login'])

        print('')

        opcao = input('Deseja conferir novamente? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def menu():

    print('***************************************')
    print('[1] Cadastrar cliente')
    print('[2] Cadastrar endereço do cliente')
    print('[3] Consultar cliente')
    print('[4] Consultar banco de dados')
    print('[0] Sair')
    print('***************************************')
    
menu()

while True:

    x = int(input('Escolha > [1] [2] [3] [4] [0]: '))

    while x > 4 or x < 0:
        x = int(input('[Erro, tente novamente!] Escolha uma opção: ')) #Caso os numeros não estejam presentes no menu, o programa irá repeti-lo. 

    if x == 1:
        cadastro()
    elif x == 2:
        cadEndereco()
    elif x == 3:
        mostrarDados()
    elif x == 4:
        mostrarClientes()
    else:
        print('')
        print('[Programa encerrado!]')
        print('')
        break
