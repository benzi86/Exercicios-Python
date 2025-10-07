from random import randint
from time import sleep
pc=randint(0,10)
tentativas=False
palpite=0
print("Tente adivinhar o número entre 0 a 10 que o computador pensou...")
print("Processando...")
sleep(1)
while not tentativas:
    jogador = int(input("Digite o número que o computador pensou:"))
    palpite+=1
    if jogador==pc:
        tentativas=True
    else:
        if jogador < pc:
            print("Mais... Tente outra vez...")
        elif jogador > pc:
            print("Menos... Tente outra vez...")
print("Parabéns você acertou com {} tentativas! ".format(palpite))




