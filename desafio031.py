viagem=int(input("Digite a distância da viagem em KM:"))
if viagem<=200:
    viagem_total=viagem*0.5
else:
    viagem_total=viagem*0.45
print("O custo da viagem será de R${:.2f}".format(viagem_total))
