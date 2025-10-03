frase= str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntar="".join(palavras)
inverso=""

for letra in range(len(juntar)-1, -1,-1):
    inverso += juntar[letra]
if inverso == juntar:
    print("A frase {} é um Palíndromo {}!".format(juntar,inverso))
else:
    print("A frase digitada {} não é um Palíndromo {}!".format(juntar,inverso))
