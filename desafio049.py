print("Tabuada")
num=int(input("Digite o numero da tabuada que quer gerar: "))
for cont in range(1,11):
    print("=*="* 6)
    print("{} x {} = {}".format(num,cont,num*cont))
print("=*=" * 6)