# vetor = [10, 20, 30, 40,50]
# print(vetor)

# -------------------------------------------------------------------------

# tamanho = int(input("Digite o tamanho do vetor: "))

# vetor = []

# for i in range(tamanho):
#     elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
#     vetor.append(elemento)

#     print("Vetor:", vetor)

# --------------------------------------------------------------------------------
# import numpy as np

# tamanho = int(input("Digite o tamanho do vetor: "))

# vetor = np.empty(tamanho, dtype=int)

# for i in range(tamanho):
#     elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
#     vetor[i] = elemento

# print("Vetor:", vetor)

# ---------------------------------------------------------------------------
# frase = "isso é uma frase de exemplo"
# palavras = frase.split()
# print(palavras)
#resultado:['isso', 'é', 'uma', 'frase', 'de', 'exemplo']

# -----------------------------------------------------------------------

# endereco = "Av Clara Gianotti de Souza, 250, Centro, Registro, SP"
# filtro = endereco.split(",")
# print(filtro)

# print(f"Nome da rua é: ", {filtro[0]})
# print(f"Numero é: ", {filtro[1]})

# ----------------------------------------------------------------------------------
# entrada = input("Digite os elementos do vetor separados por espaços: ")

# vetor = [int(x) for x in entrada.split()]

# print("Vetor:", vetor)

# --------------------------------------------------------------------------------------

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print("Elemento na primeira linha e primeira coluna:", matriz[0][0])
# print("Elemento na segunda linha e primeira coluna:", matriz[1][2])
# print("Elemento na terceira linha e primeira coluna:", matriz[2][1])

# print("Matriz")
# for linha in matriz:
#     print(linha)

# ----------------------------------------------------------------------------

# linhas = int(input("Digite o número de linhas da matriz: "))
# colunas = int(input("Digite o número de colunas da matriz: "))

# matriz_numeros = []
# for i in range(linhas):
#     linha = []
#     matriz_numeros.append(linha)
#     for j in range(colunas):
#         numero = float(input(f"Digite o número para a posição ({i}, {j}): "))
#         linha.append(numero)

#         for linha in matriz_numeros:
#             print(' '.join(map(str, linha)))

# -------------------------------------------------------------------------------------