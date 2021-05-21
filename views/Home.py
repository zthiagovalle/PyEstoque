import utils.ClearPrompt as prompt
import database.consults as consults

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

        print(consults.getIdByLogin(login))

        input("tecle entrar para continuar..")