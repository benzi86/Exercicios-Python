print("Soma dos números")
num=0
soma=0
cont=0
while num != 999:
    num = int(input("Digite um número e \33[32m[999 para parar]: \33[m"))
    if num == 999:
        break
    soma += num
    cont += 1
print("-="*25)
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")