print("Soma dos números")
num=0
soma=0
cont=0
while num!=999:
    soma+=num
    cont+=1
    num = int(input("Digite um número e \33[32m[999 para parar]: \33[m"))
    if num==999:
        cont-=1
print("-="*25)
print("Você digitou {} números e a soma entre eles foi {}".format(cont,soma))