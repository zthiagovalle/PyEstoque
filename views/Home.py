import utils.ClearPrompt as prompt
import views.AccountConfiguration as account
import views.Login
import views.Product as product
import views.Provider as provider
import views.Export as export
import views.Import as importJson

def main(login):
    while True:
        prompt.clear()
        print("\tMenu de Usuário")
        print("Opções:")
        print("1 - Configurações da conta")
        print("2 - Fornecedor")
        print("3 - Produto")
        print("4 - Exportação de dados")
        print("5 - Importação de dados")
        print("9 - Sair")
        op = input("\nInforme a sua opção: ")

        if(op == '1'):
            account.main(login)
        elif(op == '2'):
            provider.main(login)
        elif(op == '3'):
            product.main(login)
        elif (op == '4'):
            export.main(login)
        elif (op == '5'):
            importJson.main(login)
        elif(op == '9'):
            views.Login.main()
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")