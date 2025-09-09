# opcao = int(input("\n 1- Sacar \n 2- Extrato \n 3-Sair \n Escolha a opção: "))
# match opcao:
#     case 1:
#         print("Escolha a opção sacar")
#         valor = float(input("Digite o valor do saque: R$:"))
#         print(f"Sacando da sua conta o valor de {valor}...")
#     case 2:
#         print("Escolheu a opção Extrato ")
#         dias = int(input("Digite a quantidade de dias do extrato R$:"))
#         print(f"Retirando o extrato de {dias} dias...")

#     case 3:
#         exit
#     case _:
#         print("opção inválida")    

# -------------------------------------------------------------------

# opcao = (input("Digite um letra: "))

# match opcao.lower() :
#     case "a"|"e"|"i"|"o"|"u.":
#         print("Vogal")
#     case _:
#         print("Consoante")      

nivel = int(input("Informe o índice de poluição: "))

match nivel:
    case 0 | 1 | 2:
        print("Considerar Aceitável")
    case 3 | 4 | 5:
        print("Suspender Atividades Grupo 1")
    case 6 | 7:
        print("Suspender Atividades Grupo 1 e 2")
    case _:
        print("Suspender atividades de todos os grupos")            