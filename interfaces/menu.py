import os
import utils.ClearPrompt
import interfaces.Login
import interfaces.UserRegister


def main():
    while(True):
        utils.ClearPrompt.clear()
        print("\tBem vindo ao PyEstoque")
        print("Opções:")
        print("1 - Entrar no sistema")
        print("2 - Criar conta")

        op = int(input("\nInforme a sua opção: "))
        if(op not in [1, 2]):
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

        else:
            if(op == 1):
                interfaces.Login.main()
            else:
                interfaces.UserRegister.main()
