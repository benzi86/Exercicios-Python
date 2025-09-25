from math import ceil
alt=int(input("Qual a altura de sua parede:"))
larg=int(input("Qual a largura de sua parede:"))
area=alt*larg
print("\nA área de sua parede é de: {}m², você precisará de {} latas de tinta!".format(area,ceil(area/2)))


