import utils.ClearPrompt as prompt
import views.Menu as menu
import database.consults as consults
import database.inserts as inserts

def main():
    while(True):
        prompt.clear()
        print("\tCadastro de Usuário")
        print("Opções:")
        print("1 - Criar conta")
        print("9 - Voltar")

        op = input("\nInforme a sua opção: ")

        if (op == "9"):
            menu.main()
        elif (op == "1"):
            register()
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def register():
    prompt.clear()
    print("\tCadastro de Usuário")
    name = input("\nInforme seu nome completo: ")
    login = input("Informe seu usuario: ")
    password = input("Informe sua senha: ")
    confirmPassword = input("Confirme a sua senha: ")

    if(validRegister(login, password, confirmPassword)):
        inserts.createUser(name, login, password)
        print("Usuário cadastrado com sucesso !")
        input("tecle entrar para continuar..")
        menu.main()  
    else:
        print("Erro para realizar cadastrado !")
        input("tecle entrar para continuar..")
        main()

def validRegister(login, password, confirmPassword):
    if(consults.existUser(login)):
        print("\nUsuário já cadastrado!")
        return False
    
    if(password != confirmPassword):
        print("\nSenhas divergentes!")
        return False

    return True


