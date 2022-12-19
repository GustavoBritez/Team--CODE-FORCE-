numero = int(input())

resultado = 0

for i in range(numero):
    x = input()
    if x.count("1") >= 2:
        resultado = resultado+1
print(resultado)