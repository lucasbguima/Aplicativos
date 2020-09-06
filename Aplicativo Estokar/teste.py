import pandas as pd

data = pd.DataFrame({
    "Produto": [],
    "Quantidade": [],
    "Valor": []
})

def cadastrar():
    global x
    n = input("Digite o nome do produto: ")
    q = format(int(input("Digite a quantidade do produto: ")), '.0f')
    v = format(float(input("Digite o valor unitário do produto: R$")), '.2f')

    data.loc[x] = [n, q, "R$"+v]

    d = int(input("Deseja cadastrar mais produtos? (1)Sim (2)Não "))

    if d==1:
        x = x+1
        cadastrar()
    elif d==2:
        return

x = 1

cadastrar()
indice = int(input("Selecione o índice do item que deseja alterar: "))
y = data['Produto'].iloc[indice]
print(y)
n = str(input("Digite o novo nome do produto: "))

print(data)
