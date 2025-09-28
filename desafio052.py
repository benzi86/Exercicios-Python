num= int(input("Digite um número:"))
c=0
for cont in range(1, num+1):
    if num % cont==0:
        print("\33[33m",end="")
        c+=1
    else:
        print("\33[31m",end="")
    print("{} ".format(cont), end="")
if c==2:
    print("\n\33[m O número digitado {} foi dividido {} vezes, então ele é Primo!".format(num,c))
else:
    print("\n\33[m O número digitado {} foi dividido {} vezes, então ele NÃO é Primo!".format(num, c))
    