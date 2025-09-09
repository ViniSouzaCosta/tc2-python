#entrada = input('Você quer entrar ou sair?')

#if entrada == 'entrar':
#    print('você entrou no sistema');
#elif entrada == 'sair':
#    print('Você não saiu do sistema');
#else:
#    print('Você não digitou nem entrar e nem sair'); 
# 
#nota1 = float(input('informe a nota do primeiro bimestre'))   
#nota2 = float(input('informe a nota do segundo bimestre'))

#media = (nota1 + nota2) /2

#if media >= 6 :
#    print('Aprovado')
#else :
#    print('Reprovado')

# print("## Programa de empréstimo ##.  \n Responda (0- Não e 1- Sim)")

# negativo = int(input("Possui nome negativo ?"))
# if negativo == 1:
    # print("Não pode realizar empréstimo")
# else:
#    carteiraAssinada = int(input("Possui carteira assinada ?"))
# if carteiraAssinada == 0:
    # print("Não pode realizar empréstimo")
# else:
    # possuiCasaPropria = int(input("Possui casa própria ?"))
# if possuiCasaPropria == 0:
    # print("Não pode realizar empréstimo")
# else:
    # print("Conceder empréstimo")

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# numero3 = int(input("Digite o terceiro número: "))

# if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
#     exit() #encerra o programa
# if numero1 > numero2 and numero1 > numero3:
#     print("O primeiro número é o maior")
# if numero2 > numero1 and numero2 > numero3:
#     print("O segundo número é o maior")
# if numero3 > numero1 and numero3 > numero2:
#     print("O terceiro número é o maior")

# peso1 = float(input("Digite o peso da primeira pessoa: "))
# peso2 = float(input("Digite o peso da segunda pessoa: "))

# if peso1 == peso2:
#     print("Os dois tem o mesmo peso")
# elif peso1 > peso2:
#     print("Pessoa 1 é mais pesado")
# else:
#     print("Pessoa 2 é mais pesada")      
# 
# num = int(input("Informe um número: "))
 
# if num >= 0 :
#     if num % 2 == 0:
#         resultado = num * num
#         print(resultado)
#     else:
#         resultado = num * num * num
#         print(resultado)
# else:
#     print("Informe um valor positivo")

# altura1 = int(input("Digite a estatura da primeira pessoa: "))
# altura2 = int(input("Digite a estatura da segunda pessoa: "))
# altura3 = int(input("Digite a estatura da terceira pessoa: "))
 
# if altura1 > altura2 and altura1 > altura3:
#     maior = altura1
#     if altura2 > altura3:
#         meio = altura2
#         menor = altura3
#     else:
#         meio = altura3
#         menor = altura2
# elif altura2 > altura1 and altura2 > altura3:
#         maior = altura2
#         if altura1 > altura3:
#             meio = altura1
#             menor = altura3
#         else:
#             meio = altura3
#             menor = altura1               
#         else:
#         maior = altura3
#         if altura1 > altura2:
#              meio = altura1:
#              menor = altura2:
#         else:
#              meio = altura2
#              menor = altura1

#     print(f"Pessoa 1 {maior}")
#     print(f"Pessoa 2 {meio}")   
#     print(f"Pessoa 3 {menor}")   
# 

num1 = int(input("Informe o primeiro número positivo ")) 
num2 = int(input("Informe o segundo número positivo "))    


opcao = (int(input("1 - média ponderada, com pesos 2 e 3, respectivamente. \n 2 - Quadrado da soma dos 2 números. \n 3 - Cubo do menor número. Escolha uma opção: ")))

if opcao == 1:
    media = (num1 * 2 + num2 * 3) / 5
    print(f"A média é {media}")
elif opcao == 2:
    quadrado = (num1 + num1) ** 2   