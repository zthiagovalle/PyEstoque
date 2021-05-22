import utils.ClearPrompt as prompt
import views.Login as login
import views.UserRegister as register
import views.About as about
import sys

def main():
    while(True):
        prompt.clear()
        print("\tBem vindo ao PyEstoque")
        print("Opções:")
        print("1 - Entrar no sistema")
        print("2 - Criar conta")
        print("3 - Sobre o sistema")
        print("9 - Sair")
        op = input("\nInforme a sua opção: ")

        if (op == "1"):
            login.main()
        elif (op == "2"):
            register.main()
        elif (op == "3"):
            about.main()
        elif (op == "9"):
            prompt.clear()
            input("Obrigado por usar o PyEstoque :) tecle enter para sair..")
            prompt.clear()
            sys.exit()
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")
