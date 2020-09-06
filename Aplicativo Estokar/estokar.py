"""Bibliotecas"""
import pandas as pd

"""Variaveis Globais"""

data = pd.DataFrame({
    "Produto": [],
    "Quantidade": [],
    "Valor": []
})
x = len(data)

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
    
    try:
        n = str(input("Digite o nome do produto: "))    
        q = format(int(input("Digite a quantidade do produto: ")), '.0f')
        v = format(float(input("Digite o valor unitário do produto: R$")), '.2f')
    except:
        print("Você inseriu dados com formato errados!\n")
        cadastrar()

    data.loc[x] = [n, q, "R$"+v]

    d = int(input("Deseja cadastrar mais produtos? (1)Sim (2)Não "))

    if d==1:
        x = len(data)
        cadastrar()
    elif d==2:
        x = len(data)
        print(data)
        return x
    else:
        x = len(data)
        print(data)
        return x

"""Função Alterar"""
def alterar():
    indice = int(input("Selecione o índice do item que deseja alterar: "))
    y = data['Produto'].iloc[indice]
    print("\nProduto Selecionado: ", y)
    d = int(input("O item selecionado está correto? (1)Sim (2)Não (3)Voltar"))
    if d==1:
        d = int(input("O que deseja alterar? (1)Nome do Produto (2)Quantidade (3)Preço (4)Remover Produto"))
        if d==1:
            n = str(input("Digite o novo nome do produto: "))
            data['Produto'].iloc[indice] = n
            print("\n",data)
            
        elif d==2:
            q = format(int(input("Digite a nova quantidade: ")), '.0f')
            data['Quantidade'].iloc[indice] = q
            print("\n",data)
            
        elif d==3:
            v = format(float(input("Digite o novo valor: R$")), '.2f')
            data['Valor'].iloc[indice] = "R$"+v
            print("\n",data)
            
        elif d==4:
            data.drop(indice, inplace=True, axis=0)
            data.reset_index(drop=True, inplace=True)
            print("\nO produto foi removido!\n")
            print(data)
        else:
            principal()
        
    elif d==2:
        alterar()
    elif d==3:
        principal()
    else:
        alterar()

"""Função Principal"""
def principal():
    data.reset_index(drop=True, inplace=True)
    cabec()
    print("Bem vindo ao Estokar!\n")
    print("Digite o ambiente de acesso:\n\n(1)Cadastro de produtos\n(2)Ver produtos\n(3)Alterar Produtos\n(0)Sair")
    try:
        modo = int(input("Escolha um ambiente: "))
        
        if modo == 1:
            """CADASTRO DE PRODUTOS"""
            cadastrar()
            print("\nOperação Finalizada!")
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
            """ALTERAÇÃO DE PRODUTOS"""
            print("\nBem vindo a tela de alteração de produtos!\n")
            print(data)
            alterar()
            print("\nOperação Finalizada!")
            retornar()
        else:
            """ERRO"""
            print("\nVocê saiu do Estokar!")
            retornar()
    except:
        print("\nOperação Finalizada!")
        retornar()

"""Chamada de Funções"""
principal()