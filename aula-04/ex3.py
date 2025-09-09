linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for i in range(linhas):
    linha=[]
    matriz.append(linha)
    for j in range(colunas):
        capital = str(input(f"Digite o nome da capital: "))
        linha.append(capital)
