"""Bibliotecas"""
import pandas as pd

"""Variaveis Globais"""
x = 1
data = pd.DataFrame({
    "Produto": [],
    "Quantidade": [],
    "Valor": []
})

"""Função Verificar Input"""
def verificar():
    if input==

"""Função Retornar"""
def retornar():
    d = int(input("Deseja realizar outra operação? (1)Sim (2)Não "))
    if d==1:
        principal()
    elif d==2:
        d = int(input("Deseja sair e salvar seu estoque? (1)Sim (2)Não "))

        if d==1:
            print("\nVocê saiu e salvou seu estoque!\n")
        elif d==2:
            print("\nVocê saiu sem salvar seu estoque!\n")
            return
        else:
            print("Erro!")
            retornar()
    else:
        print("Erro!")
        retornar()
"""Função Cabecario"""
def cabec():
    print("=========================================================")

"""Função Cadastrar"""
def cadastrar():
    global x
    print("Bem vindo ao Cadastro de Produtos!\n")
    n = input("Digite o nome do produto: ")
    q = format(int(input("Digite a quantidade do produto: ")), '.0f')
    v = format(float(input("Digite o valor unitário do produto: R$")), '.2f')

    data.loc[x] = [n, q, "R$"+v]

    d = int(input("Deseja cadastrar mais produtos? (1)Sim (2)Não "))

    if d==1:
        x = x+1
        cadastrar()
    elif d==2:
        x = x+1
        return x
    else:
        x = x+1
        return x

"""Função Principal"""
def principal():
    cabec()
    print("Bem vindo ao Estokar!\n")
    print("Digite o ambiente de acesso:\n\n(1)Cadastro de produtos\n(2)Ver produtos\n(3)Remover Produtos\n")

    modo = int(input("Escolha um ambiente: "))
    
    if modo == 1:
        """CADASTRO DE PRODUTOS"""
        cadastrar()
        print(data)
        retornar()

    elif modo == 2:
        """TELA DE PRODUTOS"""
        print("\nBem vindo a tela de produtos!\n")
        if data.empty:
             print('Você não tem nenhum produto cadastrado!')
             retornar()
        else:
            print(data)
            retornar()
   
    elif modo == 3:
        """REMOÇÃO DE PRODUTOS"""
        print("\nBem vindo a tela de remoção de produtos!\n")
  
    else:
        """ERRO"""
        print("Erro!")
        principal()

"""Chamada de Funções"""
principal()