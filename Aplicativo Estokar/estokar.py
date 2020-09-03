def cabec():
    print("=========================================================")

def my_function():
    cabec()
    print("Bem vindo ao Aplicativo Estokar!\n")
    print("Digite o ambiente de acesso:\n\n(1)Cadastro de produtos\n(2)Ver produtos\n(3)Remover Produtos\n")

    modo = int(input("Escolha um ambiente: "))
    
    if modo == 1:
        """CADASTRO DE PRODUTOS"""
        print("\nBem vindo a tela de cadastro de produtos!\n")
        nomeproduto = input("Digite o nome do produto: ")
        qtdproduto = int(input("Digite a quantidade do produto: "))
        valorproduto = float(input("Digite o valor unitário do produto: R$"))

    elif modo == 2:
        """TELA DE PRODUTOS"""
        print("\nBem vindo a tela de produtos!\n")
   
    elif modo == 3:
        """REMOÇÃO DE PRODUTOS"""
        print("\nBem vindo a tela de remoção de produtos!\n")
  
    else:
        """ERRO"""
        print("Erro!")
        my_function()

"""Chamada de Funções"""
my_function()


