import utils.ClearPrompt as prompt
import database.consults as consults
import views.Home as home

def main(login):
    while True:
        prompt.clear()
        print("\tConfiguraçãoes da conta")
        print("Opções:")
        print("1 - Alterar senha")
        print("2 - Alterar nome")
        print("3 - Excluir Conta")
        print("9 - Voltar")
        op = input("\nInforme a sua opção: ")

        if(op == '1'):
            changePassword(login)
        elif(op == '2'):
            changeName(login)
        elif(op == '3'):
            deleteAccount(login)
        elif(op == '9'):
            home.main(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def changePassword(login):
    print("teste")

def changeName(login):
    print("teste")

def deleteAccount(login):
    print("teste")