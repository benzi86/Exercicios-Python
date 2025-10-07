print("Progressão Aritimética de 10 termos")
print("=*="* 10)
termo=int(input("Digite o primeiro termo:"))
r=int(input("Digite a razão:"))
cont = 0
while cont<10:
    print("{}".format(termo), end="→ ")
    termo+=r
    cont+=1
print("Fim")
print("=*="*20)
