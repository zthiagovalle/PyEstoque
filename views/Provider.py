import utils.ClearPrompt as prompt
import views.Home as home

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
            print("1")
        elif (op == "2"):
            print("2")
        elif (op == "3"):
            print("3")
        elif (op == "4"):
            print("4")
        elif (op == "9"):
            home.main(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")