

def getProvider(providerList):
    lstProviderDic = []
    for provider in providerList:
        providerDic = {'id':provider[0], 'nome':provider[1], 'telefone':provider[2], 'endereco':provider[3], 'usuario_id':provider[4]}
        lstProviderDic.append(providerDic)
    return lstProviderDic

def getProduct(productList):
    lstProductDic = []
    for product in productList:
        productDic = {'id':product[1], 'nome':product[2], 'valor_venda':product[3], 'valor_compra':product[4], 'quantidade_estoque':product[5], 'fornecedor_id':product[6], 'usuario_id':product[7]}
        lstProductDic.append(productDic)
    return lstProductDic
