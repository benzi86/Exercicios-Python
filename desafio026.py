frase=str(input("Digite uma frase: ")).upper()
print("O número de vezes que a palavra 'A' aparece na frase é de: {} vezes".format(frase.count("A")))
print("A primeira vez que a palavra 'A' aparece nessa frase é na posição: {}".format(frase.find("A")))
print("A última vez que a plavra 'A' aparece nessa frase é na posição: {}".format(frase.rfind("A")))
