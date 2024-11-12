#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.

list = []

print('digite 20 números inteiros.')
for i in range (1, 21):
    numero = int(input(f"digite o {i}°: "))
    list.append(numero)

print("a lista é:", list)

par = [x for x in list if x%2==0]
print("a lista dos números pares:", par)

impar = [x for x in list if x%2!=0]
print("a lista dos números ímpares:", impar)

