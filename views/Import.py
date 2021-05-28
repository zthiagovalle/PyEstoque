import views.Home as home
import utils.ClearPrompt as prompt
import database.inserts as inserts
import database.consults as consults
import json
import os

def main(login):
    while True:
        prompt.clear()
        print("\tImportação de dados")
        print("Opções:")
        print("1 - Importar")
        print("9 - Voltar")

        op = input("\nInforme a sua opção: ")

        if (op == "9"):
            home.main(login)
        elif(op == "1"):
            importJson(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def importJson(login):

    datatotalProviders = []
    path_dir = os.path.join(os.sep, os.getcwd(), "import")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('Fornecedores.json')):
                with open(os.path.join(dirname, filename), 'r', encoding='utf8') as f:
                    try:
                        data = json.load(f)
                        if(data != []):
                            for provider in data:
                                name = provider['nome']
                                phoneNumber = provider['telefone']
                                address = provider['endereco']
                                if(inserts.createProvider(login, name, phoneNumber, address)):
                                    print("Fornecedor cadastrado com sucesso.")
                                else:
                                    print("Falha ao cadastrar fornecedor.")
                    except:
                        print("Ocorreu erro na leitura do json")

    datatotalProducts = []
    path_dir = os.path.join(os.sep, os.getcwd(), "import")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('Produtos.json')):
                with open(os.path.join(dirname, filename), 'r', encoding='utf8') as f:
                    try:
                        data = json.load(f)
                        if(data != []):
                            for product in data:
                                name = product['nome']
                                salePrice = product['valor_venda']
                                purchasePrice = product['valor_compra']
                                providerId = product['fornecedor_id']
                                if(consults.getProviderById(providerId, login) != []):
                                    if(inserts.createProduct(login, providerId, name, purchasePrice, salePrice)):
                                        print("Produto cadastrado com sucesso.")
                                    else:
                                        print("Falha ao cadastrar produto.")
                                else:
                                    print("Falha ao cadastrar produto. Fornecedor não existe.")
                    except:
                        print("Ocorreu erro na leitura do json")
               
    input("tecle entrar para continuar..")