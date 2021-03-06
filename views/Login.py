import utils.ClearPrompt as prompt
import views.Menu as menu
import database.consults as consults
import views.Home as home

def main():
    while True:
        prompt.clear()
        print("\tLogin de Usuário")
        print("Opções:")
        print("1 - Logar")
        print("9 - Voltar")

        op = input("\nInforme a sua opção: ")

        if (op == "9"):
            menu.main()
        elif(op == "1"):
            login()
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def login():
    prompt.clear()
    print("\tLogin de Usuário")
    login = input("\nInforme seu usuário: ")
    password = input("Informe sua senha: ")
    
    if(consults.authenticate(login, password)):
        print("\nAutenticação concluida!")
        input("tecle entrar para acessar o menu de usuário..")
        home.main(login)
    else:
        print("\nConta não localizada.")
        input("tecle entrar para continuar..")
        main()
