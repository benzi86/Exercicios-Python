print("-="*25)
print("Gerador de Tabuadas!")
print("-="*25)
tabuada=0

while True:
    tabuada = int(input("Qual tabuada quer gerar?"))
    if tabuada < 0:
        print("Programa encerrado!")
        break
    cont = 0
    num=0
    print("=" * 20)
    for cont in range(0,11):
        print(f"{tabuada} x {cont} = {num}")
        cont += 1
        num=tabuada*cont
    print("=" * 20)



