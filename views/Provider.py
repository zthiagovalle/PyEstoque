import utils.ClearPrompt as prompt
import views.Home as home
import database.inserts as inserts
import database.consults as consults

def main(login):
    while(True):
        prompt.clear()
        print("\t Fornecedor")
        print("Opções:")
        print("1 - Cadastrar Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
        print("9 - Voltar")
        op = input("\nInforme a sua opção: ")

        if (op == "1"):
            register(login)
        elif (op == "2"):
            print("2")
        elif (op == "3"):
            getProviders(login)
        elif (op == "4"):
            deleteProvider(login)
        elif (op == "9"):
            home.main(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def register(login):
    prompt.clear()
    print("\t Cadastro de Fornecedor")
    name = input("\nNome: ")
    phoneNumber = input("Telefone: ")
    address = input("Endereço: ")

    if(inserts.createProvider(login, name, phoneNumber, address)):
        print("Fornecedor cadastrado com sucesso!")
        input("tecle entrar para continuar..")

def getProviders(login):
    prompt.clear()
    print("\tFornecedores Cadastrados")
    providers = consults.getProviders(login)
    if(providers != []):
        for provider in providers:
            print("---------------------------------------------")
            print(f"Nome: {provider[1]}")
            print(f"Telefone: {provider[2]}")
            print(f"Endereço: {provider[3]}")
            print("---------------------------------------------")
        input("tecle entrar para continuar..")
    else:
        print("Não existe fornecedores cadastrados")
        input("tecle entrar para continuar..")

def deleteProvider(login):
    prompt.clear()
    print("\tDeleção de Fornecedores")
    providers = consults.getProviders(login)
    if(providers != []):
        for provider in providers:
            print("---------------------------------------------")
            print(f"ID: {provider[0]}")
            print(f"Nome: {provider[1]}")
            print(f"Telefone: {provider[2]}")
            print(f"Endereço: {provider[3]}")
            print("---------------------------------------------")
        providerId = input("Digite o id do fornecedor que deseja excluir: ")
    else:
        print("Não existe fornecedores cadastrados")
        input("tecle entrar para continuar..")   