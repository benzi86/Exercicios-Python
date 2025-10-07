print("*=*Calculando Fatorial*=*")
fat=1
num=int(input("Digite o número para calcular o Fatorial:"))
print("Fatorial de {}! =".format(num),end="")
for cont in range(num, 0, -1):
    print("{}".format(cont), end=" ")
    print("X" if cont > 1 else "=", end=" ")
    fat*=cont
print("{}".format(fat),end="")