contatos = []

while True:
    print("\n===== AGENDA DE CONTATOS =====")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        contatos.append({"nome": nome, "telefone": telefone})
        print("Contato adicionado com sucesso!")

    elif opcao == "2":
        if len(contatos) == 0:
            print("Nenhum contato cadastrado.")
        else:
            print("\nLista de contatos:")
            for i, contato in enumerate(contatos):
                print(f"{i} - {contato['nome']} | {contato['telefone']}")

    elif opcao == "3":
        indice = int(input("Digite o número do contato para remover: "))
        if 0 <= indice < len(contatos):
            contatos.pop(indice)
            print("Contato removido!")
        else:
            print("Índice inválido!")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
