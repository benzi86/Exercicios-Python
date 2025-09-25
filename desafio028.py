#Programa onde o computador pensa em um número e o jogador tenta acertar
from random import randint
from time import sleep
print("O computador pensou em um número entre 0 e 5...")
computador=randint(0,5)
jogador=int(input("Digite qual o número que o computador pensou:"))
print("PROCESSANDO...")
sleep(2)
if jogador==computador:
    print("Parabéns você acertou!")
else:
    print("Que pena você errou, eu pensei no número {}!".format(computador))