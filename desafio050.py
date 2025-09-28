print("=*="* 10)
print("Somatória dos números pares:")
print("=*="* 10)
soma=0
c=0
for cont in range(1,7):
    num=int(input("Digite o {} valor:".format(cont)))
    if num%2==0:
        soma+=num
        c+=1
print("Os números pares informados foram {} e a soma deles é: {}".format(c, soma))
