linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for i in range(linhas):
    linha=[]
    matriz.append(linha)
    for j in range(colunas):
        numero = int(input(f"Digite o número para a {i+1},{j+1} posição: "))
        linha.append(numero)

cont = 0
for mat in matriz :
    for linha in mat:
        if linha > 10:
            print(linha)
            cont +=1
print(f"Valores maiores que 10: {cont}")