import utils.ClearPrompt as prompt
import sqlite3


def main():
    con = sqlite3.connect('./database/db.db')

    op = 0
    while op not in [1, 2, 3]:
        prompt.clear()
        print("\tLogin\n")
        print("Opções:")
        print("1 - Logar")
        print("2 - Criar conta")
        print("3 - Alterar senha")
        op = int(input())
        if(op not in [1, 2, 3]):
            print("Opção inválida")
            input("Enter para continuar")
        else:
            if op == 1:
                # TODO logar
                login = input("Digite seu login: ")
                # TODO aqui podemos procurar uma lib para colocar *** ao inves
                # de texto, mas tem que instalar com pip install
                senha = input("Digite sua senha: ")

                if con.execute("select count(*) as existe from usuario where login=? and senha=?", [login, senha]).fetchone()[0] == 1:
                    # TODO fazer algo ao logar
                    print(f"Bem vindo, {login}!")
                    input()
                    # TODO guardar essa variavel globalmente
                    logado = {login: login}
                else:
                    print("Credenciais incorretas")
                    input("Pressione enter para voltar ao menu")

                pass
            elif op == 2:
                nome = input("Digite seu nome")
                login = input("Digite seu login")
                senha = input("Digite sua senha")
                con.execute('insert into usuario (nome, login, senha) values (?, ?, ?)', [
                             nome, login, senha])
                con.commit()
                input("Usuario criado com sucesso, pressione enter para continuar")

                pass
            elif op == 3:
                # TODO alterar senha do usuario logado
                pass
