print("=*="*18)
print("Analisando se as retas podem formar um triângulo")
print("=*="*18)
reta1=float(input("Digite o valor da primeira reta: "))
reta2=float(input("Digite o valor da segunda reta: "))
reta3=float(input("Digite o valor da terceira reta: "))
if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    print("As retas digitadas PODEM formar um triângulo!")
else:
    print("As retas digitadas NÃO podem formar um triângulo, tente outras combinações!")