n = int(input())
while (n < 1 or n > 1000):
    n = int(input())

matriz = []


for i in range(n):
    matriz.append([])
    for j in range(3):
        numero = int(input())
        matriz[i].append(numero)

    resultado = 0
for i in range(n):
    contador = 0
    for j in range(3):
        print(matriz[i][j], end = " ")
        if(matriz[i][j] == 1):
            contador = contador +1
            if(contador == 2):
                resultado = resultado +1
    print()

print(resultado)


