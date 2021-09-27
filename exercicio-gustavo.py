
# 1º Faça um programa que pergunta a idade do usuário e informe se ele está apto a votar ou não.

idade = int(input("Insira sua idade: "))

if idade < 16:
    print("Voto inválido!")
elif 18 > idade > 70: 
    print("Voto opcional!")
elif 18 <= idade <= 70:
    print("Voto obrigatório!")
 
# 2º Faça um Programa que leia três números inteiros e mostre o maior deles.

a = int(input("Insira um valor inteiro de a: "))
b = int(input("Insira um valor inteiro de b: "))
c = int(input("Insira um valor inteiro de c: "))

if  c <= a >= b:
    maior = a
elif c <= b >= a:
    maior = b
elif b <= c >= a:
    maior = c

print(f"O maior valor é {maior}")

# 3º Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

a = int(input("Insira um valor inteiro de a: "))
b = int(input("Insira um valor inteiro de b: "))
c = int(input("Insira um valor inteiro de c: "))

if  c <= a >= b:
    maior = a
elif c <= b >= a:
    maior = b
elif b <= c >= a:
    maior = c

print(f"O maior valor é {maior}")

if c >= a <= b:
    menor = a
elif c >= b <= a:
    menor = b
elif a >= c <= b:
    menor = c

print(f"O menor valor é {menor}")


# 4º Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.

lista = []
n = 0 
while n <101:
    lista.append(n)
    n += 1 
print(lista)

# 5º Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.


lista = []
limite = int(input("Insira um numero limite: "))
n = 0 
while n < limite + 1:
    lista.append(n)
    n += 1 
print(lista)


# 6º Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

lista = []
n = 1 
while n <= 5:
    lista.append(input(f"Insira o nome {n}: "))
    n += 1 
print(lista)

# 7º Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

a = int(input("Insira o primeiro valor para a soma: "))
b = int(input("Insira o segundo valor para a soma: "))
soma = a + b
print(soma)

pergunta = input("Deseja fazer nova soma? (digite Sim ou Não) ") 

while pergunta == "SIM" or pergunta == "sim" or pergunta == "Sim":   
    a = int(input("Insira o primeiro valor para a soma: "))
    b = int(input("Insira o segundo valor para a soma: "))
    soma = a + b
    print(soma)
    pergunta = input("Deseja fazer nova soma? (digite Sim ou Não) ")
PRINT("Fim")

# 8º Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número indeterminado de pessoas enquanto quiser e os mostre na tela ao finalizar.

lista = []
lista.append(input("Insira o nome para cadastro: "))
pergunta = input("Deseja fazer novo cadastro? (digite Sim ou Não) ") 

while pergunta == "SIM" or pergunta == "sim" or pergunta == "Sim" or pergunta == "S" or pergunta == "s":   
    lista.append(input("Insira o nome para cadastro: "))
    pergunta = input("Deseja fazer novo cadastro? (digite Sim ou Não) ") 

print(lista)
print("Fim")


# 9º Faça um programa que imprima a quantidade de números pares entre dois números da sua escolha.

numero1 = int(input('Digite o numero do limite inferior: '))
numero2 = int(input('Digite o numero do limite superior: '))
lista = []
n = numero1
while n <= numero2:
    if (n%2) == 0:
        lista.append(n)
        n += 2
    elif (n%2) != 0:
        n += 1

print(lista)

# 10º Faça um programa que imprima a soma de todos os números pares entre dois números da sua escolha.

numero1 = int(input('Digite o numero do limite inferior: '))
numero2 = int(input('Digite o numero do limite superior: '))
lista = []
n = numero1
while n <= numero2:
    if (n%2) == 0:
        lista.append(n)
        n += 2
    elif (n%2) != 0:
        n += 1

print(lista)
print(sum(lista))


