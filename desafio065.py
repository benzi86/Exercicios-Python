print("-="*25)
print("Média de números digitados")
print("-="*25)
num=0
cont=0
confirmar=""
med=0
maior=0
menor=0
while confirmar in "Ss":
    num = int(input("Digite um número:"))
    confirmar=str(input("Quer continuar?[S/N]")).upper().strip()[0]
    med+=num
    cont+=1
    if cont == 1:
     maior = num
     menor = num
    else:
        if num>maior:
            maior=num
        if num<menor:
         menor=num
med = med/cont
print("Você digitou \33[32m{}\33[m números e a média foi \33[31m{:.2f}\33[m".format(cont, med))
print("O maior número digitado foi: \33[34m{}\33[m e o menor número foi \33[31m{}\33[m".format(maior,menor))
print("-="*25)