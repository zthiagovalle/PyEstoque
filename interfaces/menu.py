import utils.ClearPrompt
import interfaces.Login
import interfaces.UserRegister

def main():
    while(True):
        utils.ClearPrompt.clear()
        print("\tBem vindo ao PyEstoque")
        print("Opções:")
        print("1 - Entrar no sistema.")
        print("2 - Criar conta.")

        op = input("\nInforme a sua opção: ")

        if (op == "1"):
            interfaces.Login.main()
        elif (op == "2"):
            interfaces.UserRegister.main()
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")