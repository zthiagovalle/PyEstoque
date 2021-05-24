import utils.ClearPrompt as prompt
import views.Home as home
import database.inserts as inserts
import database.consults as consults
import database.deletes as deletes

def main(login):
    while(True):
        prompt.clear()
        print("\t Produto")
        print("Opções:")
        print("1 - Cadastrar Produto")
        print("2 - Alterar Produto")
        print("3 - Listar Produtos")
        print("4 - Excluir Produto")
        print("5 - Controle de Estoque")
        print("9 - Voltar")
        op = input("\nInforme a sua opção: ")

        if (op == "1"):
            register(login)
        elif (op == "2"):
            print("2")
        elif (op == "3"):
            getProducts(login)
        elif (op == "4"):
            deleteProduct(login)
        elif (op == "9"):
            home.main(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def register(login):
    prompt.clear()
    print("\t Cadastro de Produto")

    providers = consults.getProviders(login)
    if(providers != []):
        for provider in providers:
            print("---------------------------------------------")
            print(f"ID: {provider[0]}")
            print(f"Nome: {provider[1]}")
            print(f"Telefone: {provider[2]}")
            print(f"Endereço: {provider[3]}")
            print("---------------------------------------------")

        try:
            providerId = int(input("Digite o id do fornecedor do produto que deseja cadastrar: "))
        except:
            print("Você digitou um id invalido")
            input("tecle entrar para continuar..") 
            main(login)
        
        providerToChange = consults.getProviderById(providerId, login)
        if(providerToChange != []):
            name = input("\nNome: ")
            purchasePrice = input("Valor de Compra R$")
            salePrice = input("Valor de Venda R$")
            if(inserts.createProduct(login, providerId, name, purchasePrice, salePrice)):
                print("Produto cadastrado com sucesso!")
                input("tecle entrar para continuar..")
                main(login)
            else:
                print("Não foi possível cadastrar o produto.")
                input("tecle entrar para continuar..")
                main(login)
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe fornecedores cadastrados, então não é possivel cadastrar um produto.")
        input("tecle entrar para continuar..")
        main(login)

def getProducts(login):
    prompt.clear()
    print("\tProdutos Cadastrados")
    products = consults.getProducts(login)
    if(products != []):
        for product in products:
            print("---------------------------------------------")
            print(f"Nome do Fornecedor: {product[0]}")
            print(f"Nome Produto: {product[2]}")
            print(f"Valor de Venda R${product[3]}")
            print(f"Valor de Compra R${product[4]}")
            print(f"Quantidade em estoque: {product[5]}")
            print("---------------------------------------------")
        input("tecle entrar para continuar..")
    else:
        print("Não existe produtos cadastrados")
        input("tecle entrar para continuar..")

def deleteProduct(login):
    prompt.clear()
    print("\tDeleção de Produtos")
    products = consults.getProducts(login)
    if(products != []):
        for product in products:
            print("---------------------------------------------")
            print(f"Nome do Fornecedor: {product[0]}")
            print(f"Id do Produto: {product[1]}")
            print(f"Nome Produto: {product[2]}")
            print(f"Valor de Venda R${product[3]}")
            print(f"Valor de Compra R${product[4]}")
            print(f"Quantidade em estoque: {product[5]}")
            print("---------------------------------------------")

        try:
            productId = int(input("Digite o id do produto que deseja excluir: "))
        except:
            print("Você digitou um id invalido")
            input("tecle entrar para continuar..") 
            main(login)
        
        productToDelete = consults.getProductById(productId, login)
        if(productToDelete != []):
            deletes.deleteProductById(login, productId)
            print("Produto Excluido com sucesso!")
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe produtos cadastrados")
        input("tecle entrar para continuar..")