# Menu

print("*************************************")
print()
print("########### MENU INICIAL ############")
print()
print("*************************************")
print(" 1 - Incluir usuario ")
print(" 2 - Excluir usuario")
print(" 3 - Consultar usuario")
print(" 4 - Alterar usuario")
print(" 5 - listar todos os usuarios cadastrados")
print(" 9 - Sair")

# Laço de repetição

while True:

    opcao = int(input("Digite o número da opção para prosseguir: "))

    if opcao == 1:
        print("*************************************")
        print("Opção 1 - Incluir usuário Selecionada")
        print("*************************************")
    elif opcao == 2:
        print("*************************************")
        print("Opção 2 - Excluir usuário Selecionada")
        print("*************************************")
    elif opcao == 3:
        print("*************************************")
        print("Opção 3 - Consultar usuário Selecionada")
        print("*************************************")
    elif opcao == 4:
        print("*************************************")
        print("Opção 4 - Alterar usuário Selecionada")
        print("*************************************")
    elif opcao == 5:
        print("*************************************")
        print("Opção 5 - Listar todos os usuários cadastrados Selecionada")
        print("*************************************")
    elif opcao == 9:
        print("*************************************")
        print("Opção 9 - Sair Selecionada")
        print("*************************************")
        break  
    else:
        print("Opção inválida! Tente novamente.")

    




    
