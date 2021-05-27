import views.Home as home
import utils.ClearPrompt as prompt
import database.consults as consults
import utils.ConvertListToListDic as convert
import json
import os
import zipfile as zip

def main(login):
    while True:
        prompt.clear()
        print("\tExportação de dados")
        print("Opções:")
        print("1 - Exportar")
        print("9 - Voltar")

        op = input("\nInforme a sua opção: ")

        if (op == "9"):
            home.main(login)
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
        home.main(login)
    
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

    path_zip = os.path.join(os.sep, os.getcwd(), "export\export.zip")
    path_dir = os.path.join(os.sep, os.getcwd().replace("views", ''), "export")

    zf = zip.ZipFile(path_zip, "w")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('.json')):
                zf.write(os.path.join(dirname, filename))
                os.remove(os.path.join(dirname, filename))
    zf.close()

    print("\nExportação concluida com sucesso!..")
    print("Os dados exportados estão na pasta export")
    input("tecle entrar para continuar..")
    
