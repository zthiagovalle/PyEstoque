import views.Menu as menu
import utils.ClearPrompt as prompt
import database.consults as consults
import utils.ConvertListToListDic as convert
import json
import os
import zipfile

def main(login):
    while True:
        prompt.clear()
        print("\tExportação de dados")
        print("Opções:")
        print("1 - Exportar")
        print("9 - Voltar")

        op = input("\nInforme a sua opção: ")

        if (op == "9"):
            menu.main()
        elif(op == "1"):
            export(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def export(login):
    providerList = consults.getProviders(login)
    produtctList = consults.getProducts(login)
    if(providerList == [] and produtctList == []):
        print("Você não tem dados para Exportar!")
        input("tecle entrar para continuar..")
        menu.main()
    
    if(providerList != []):
        dic = convert.getProvider(providerList)
        file = open("./export/Fornecedores.json", "w")
        json.dump(dic, file, indent=4)
        file.close()
    
    if(produtctList != []):
        dic = convert.getProduct(produtctList)
        file = open("./export/Produtos.json", "w")
        json.dump(dic, file, indent=4)
        file.close()

    print("\nExportação concluida com sucesso!..")
    print("Os dados exportados estão na pasta export")
    input("tecle entrar para continuar..")
    
