import utils.ClearPrompt as prompt
import views.Home as home
import database.inserts as inserts
import database.consults as consults
import database.deletes as deletes
import database.updates as updates

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
            changeProduct(login)
        elif (op == "3"):
            getProducts(login)
        elif (op == "4"):
            deleteProduct(login)
        elif (op == "5"):
            controlProduct(login)
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

def changeProduct(login):
    prompt.clear()
    print("\tAlteração de Produto")
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
        
        productToChange = consults.getProductById(productId, login)
        if(productToChange != []):
            print("\nCaso não deseje alterar o campo digite 0")
            newName = input("\nNovo nome: ")
            newPurchasePrice = input("Novo Valor de Compra R$")
            newSalePrice = input("Novo Valor de Venda R$")

            if(newName == '0' and newPurchasePrice == '0' and newSalePrice == '0'):
                print("Produto não teve alterações.")
                input("tecle entrar para continuar..")
                main(login)

            if(newName == '0'):
                newName = productToChange[0][1]
            
            if(newSalePrice == '0'):
                newSalePrice = productToChange[0][2]

            if(newPurchasePrice == '0'):
                newPurchasePrice = productToChange[0][3]

            updates.changeProduct(productId, newName, newPurchasePrice, newSalePrice, productToChange[0][5])
            print("Produto Alterado com sucesso!")
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe Produtos cadastrados")
        input("tecle entrar para continuar..")
    

def controlProduct(login):
    prompt.clear()
    print("\tControle do Estoque de produtos")
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
            productId = int(input("Digite o id do produto que deseja alterar o estoque: "))
        except:
            print("Você digitou um id invalido")
            input("tecle entrar para continuar..") 
            main(login)
        
        productToChange = consults.getProductById(productId, login)
        if(productToChange != []):
            print("\nDigite um número inteiro positivo para somar a quantidade de estoque do produto.\nDigite um número inteiro negativo para subtrair a quantidade de estoque do produto.")
            try:
                quantity = int(input("Digite: "))
                if(quantity > 0):
                    stokQuantity = productToChange[0][4] + quantity
                else:
                    if(quantity + productToChange[0][4] < 0):
                        print("Você quer tirar mais do que o produto tem.")
                        input("tecle entrar para continuar..") 
                        main(login)
                    else:
                        stokQuantity = productToChange[0][4] + quantity

                updates.changeProduct(productId, productToChange[0][1], productToChange[0][3], productToChange[0][2], stokQuantity)
                
                print("Estoque atualizado com sucesso!")
            except:
                print("Você digitou um número invalido")
                input("tecle entrar para continuar..") 
                main(login)
        else:
            print("Você digitou um id invalido")

        input("tecle entrar para continuar..") 

    else:
        print("Não existe produtos cadastrados")
        input("tecle entrar para continuar..")