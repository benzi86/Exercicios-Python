print("Progressão Aritimética de 10 termos")
print("=*="* 10)
termo=int(input("Digite o primeiro termo:"))
r=int(input("Digite a razão:"))
decimo=termo+(10-1)*r
for cont in range(termo, decimo+r, r):
   print("{} ".format(cont),end="→ ")
print("Fim")
print("=*="*20)

