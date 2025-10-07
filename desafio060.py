print("*=*Calculando Fatorial*=*")
num=int(input("Digite um número:"))
cont=num
fatorial=1
print("O Fatorial de \33[34m{}!\33[m= ".format(num),end=" ")
while cont>0:
    print("{}".format(cont),end=' ')
    print("X" if cont>1 else "=",end=' ')
    fatorial *= cont
    cont -= 1
print("\33[32m{}\33[m".format(fatorial),end=' ')

print("\nFim do programa!")