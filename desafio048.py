str(print("Números Multiplos de 3"))
soma=0
c=0
for cont in range(1,501,2):
    if cont%3==0:
        soma=soma+cont
        c = c + 1
print("A soma de todos os {} valores multiplos de 3 é: {}".format(c,soma))