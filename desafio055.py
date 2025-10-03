print("Maior e Menor peso")
menor=0
maior=0
for pessoa in range (1,6):
    peso=float(input(" Digite o peso da {}º pessoa:".format(pessoa)))
    if pessoa==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
         maior=peso
        if peso<menor:
         menor=peso
print("O maior peso digitado foi {} KG e o menor peso foi de {} KG".format(maior,menor))
