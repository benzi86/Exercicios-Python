print("Progressão Aritimética")
print("=*="* 10)
termo=int(input("Digite o primeiro termo:"))
r=int(input("Digite a razão:"))
cont = 0
escolha= 10
total=0
while escolha != 0:
    total = total + escolha
    while cont<total:
        print("{}".format(termo), end="→ ")
        termo+=r
        cont+=1
    print("Pausa")
    escolha=int(input("Quantos termos quer mostrar?"))
print("A PA teve {} termos impresos".format(total))
print("FIM")
print("=*="*20)
