"""Escreva um programa para criar uma lista de tuplas contendo quatro itens relativos a uma mesma pessoa: (nome, email, dia nascimento, mês nascimento).

Implemente funções para fazer um cadastro:

- incluir ( )
- consultar ( )
- excluir ( )
- listar ( )
- atualizar ( )"""

db = [('Luiz', 'luiz@mail.com', 15, 8), ('Gabriel', 'gabriel@mail.com', 10, 2), ('Joao', 'joao@Mail.com', 10, 9)]
while True:
    print("=="*20)
    print("""
    Bem-Vindo. Escolha uma opção.
    1 - Incluir ( )
    2 - Consultar ( )
    3 - Excluir ( )
    4 - Listar ( )
    5 - Atualizar ( )
    6 - Exit ( )
    """)
    print("==" * 20)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Insira o nome: ")
        email = input("Insira o e-mail: ")
        dia_nascimento = int(input("Digite o dia do nascimento: "))
        mes_nascimento = int(input("Digite o mes do nascimento: "))

        usuario = (nome, email, dia_nascimento, mes_nascimento)
        db.append(usuario)
        print("Usuário cadastrado com sucesso")
        print(db)
    elif opcao == 2:
        """#Entrar dentro DB
           #Entrar dentro da tupla
           #Entrar dentro da Lista"""

        get_mail = input("Informe o e-mail do usuário: ")
        for tuplas in db:
            if (tuplas[1]) == get_mail:
                print("O nome do usuário é: ", tuplas[0])
                print("O e-mail do usuário é: ", tuplas[1])
                print("O dia do nascimento do usuário é: ", tuplas[2])
                print("O mês de nascimento do usuário é: ", tuplas[3])


    elif opcao == 3:
        """
        #Acessar a tupla
        #Excluir a tupla
        """
        get_mail = input("Informe o e-mail do usuário: ")
        for tuplas in db:
            if (tuplas[1]) == get_mail:
                db.remove(tuplas)

#Listar cada usuário
    elif opcao == 4:
        for usuario in db:
            print("==" * 10)
            print("O nome do usuário é: ", usuario[0])
            print("O e-mail do usuário é: ", usuario[1])
            print("O dia de nascimento é: ", usuario[2])
            print("O mês de nascimento é: ", usuario[3])
            print("==" * 10)

    elif opcao == 5:
        """#Acessar a tupla
           #Excluir a tupla
           #Criar uma nova tupla"""

        get_mail = input("Informe o e-mail do usuário: ")
        for tuplas in db:
            if get_mail in tuplas:
                db.remove(tuplas)

                nome = input("Insira o nome: ")
                email = input("Insira o e-mail: ")
                dia_nascimento = int(input("Digite o dia do nascimento: "))
                mes_nascimento = int(input("Digite o mes do nascimento: "))
                usuario = (nome, email, dia_nascimento, mes_nascimento)
                db.append(usuario)
                print("Usuário cadastrado com sucesso")

    elif opcao == 6:
        break