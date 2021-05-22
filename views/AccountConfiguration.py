import utils.ClearPrompt as prompt
import database.consults as consults
import views.Home as home
import database.updates as updates
import database.deletes as deletes
import views.Login

def main(login):
    while True:
        prompt.clear()
        print("\tConfiguraçãoes da conta")
        print("Opções:")
        print("1 - Alterar senha")
        print("2 - Excluir Conta")
        print("9 - Voltar")
        op = input("\nInforme a sua opção: ")

        if(op == '1'):
            changePassword(login)
        elif(op == '2'):
            deleteAccount(login)
        elif(op == '9'):
            home.main(login)
        else:
            print("Você informou um opção inválida !")
            input("tecle entrar para continuar..")

def changePassword(login):
    prompt.clear()
    oldPassword = input("Informe sua senha atual: ")
    newPassword = input("Digite sua nova senha: ")
    confirmNewPassword = input("Confirme a sua nova senha: ")

    if(validchangePassword(login, oldPassword, newPassword, confirmNewPassword)):
        updates.changePassword(login, newPassword)
        print("Senha alterada com sucesso. !")
        input("tecle entrar para continuar..")
    else:
        print("Erro para mudança de senha !")
        input("tecle entrar para continuar..")
        main(login)

def deleteAccount(login):
    print("\nCuidado!")
    confirm = input("Voce confirma a exclusão da conta? digite SIM para confirmar a exclusão: ")

    if(confirm == "SIM"):
        deletes.deleteAccount(login)
        input("Conta excluida! tecle enter para continuar..")
        views.Login.main()
    else:
        main(login)

def validchangePassword(login, oldPassword, newPassword, confirmNewPassword):
    if(consults.authenticate(login, oldPassword) == False):
        print("A Senha autal não confere!")
        return False
    
    if(newPassword != confirmNewPassword):
        print("Senhas divergentes!")
        return False
    
    return True