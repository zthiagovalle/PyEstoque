import utils.ClearPrompt as prompt
import views.Home as home
import database.inserts as inserts
import database.consults as consults
import database.deletes as deletes
import database.updates as updates

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
            changeProvider(login)
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

        try:
            providerId = int(input("Digite o id do fornecedor que deseja excluir: "))
        except:
            print("Você digitou um id invalido")
            input("tecle entrar para continuar..") 
            main(login)
        
        providerToDelete = consults.getProviderById(providerId, login)
        if(providerToDelete != []):
            deletes.deleteProviderById(login, providerId)
            print("Fornecedor Excluido com sucesso!")
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe fornecedores cadastrados")
        input("tecle entrar para continuar..")

def changeProvider(login):
    prompt.clear()
    print("\tAlteração de Fornecedores")
    providers = consults.getProviders(login)
    if(providers != []):
        for provider in providers:
            print("---------------------------------------------")
            print(f"ID: {provider[0]}")
            print(f"Nome: {provider[1]}")
            print(f"Telefone: {provider[2]}")
            print(f"Endereço: {provider[3]}")
            print("---------------------------------------------")

        try:
            providerId = int(input("Digite o id do fornecedor que deseja alterar: "))
        except:
            print("Você digitou um id invalido")
            input("tecle entrar para continuar..") 
            main(login)
        
        providerToChange = consults.getProviderById(providerId, login)
        if(providerToChange != []):
            print("\nCaso não deseje alterar o campo digite 0")
            newName = input("\nNovo nome: ")
            newPhoneNumber = input("Novo telefone: ")
            newAddress = input("Novo endereço: ")

            if(newName == '0' and newPhoneNumber == '0' and newAddress == '0'):
                print("Fornecedor não teve alterações.")
                input("tecle entrar para continuar..")
                main(login)

            if(newName == '0'):
                newName = providerToChange[0][1]
            
            if(newPhoneNumber == '0'):
                newPhoneNumber = providerToChange[0][2]

            if(newAddress == '0'):
                newPhoneNumber = providerToChange[0][3]

            updates.changeProvider(providerId, newName, newPhoneNumber, newAddress)
            print("Fornecedor Alterado com sucesso!")
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe fornecedores cadastrados")
        input("tecle entrar para continuar..")    