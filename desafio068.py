import time
import pygame
pygame.init()
vitoria=pygame.mixer.Sound('victory_music.mp3')
defeat=pygame.mixer.Sound('game_over.mp3')
from random import randint
print("=" * 20)
print("Jogo Par ou Impar!")
print("=" * 20)
cont=0
while True:
    jogador=int(input("Digite um valor: "))
    escolha=str(input("Escolha Par ou Impar [P/I]:").upper().strip())
    while escolha not in "PI":
       print("\33[3m\33[31mINVÁLIDO!, escolha [P'Para PAR' ou I 'Para IMPAR']\33[m")
       escolha = str(input("Escolha Par ou Impar [P/I]:").upper().strip())
    computador=randint(0,10)
    soma=jogador+computador
    if escolha == "P" and soma % 2 == 0:
        print(f"Você jogou \33[32m{jogador}\33[m e o computador jogou \33[31m{computador}\33[m. Total de {soma} deu PAR")
        print("Jogador venceu!")
        vitoria.play()
        time.sleep(0)
        cont+=1
    elif escolha == "I" and soma % 2!= 0:
        print(f"Você jogou \33[32m{jogador}\33[m e o computador jogou \33[31m{computador}\33[m. Total de {soma} deu IMPAR")
        print("Jogador venceu!")
        vitoria.play()
        time.sleep(0)
        cont+=1
    elif escolha == "P" and soma % 2 != 0:
        print(f"Você jogou \33[32m{jogador}\33[m e o computador jogou \33[31m{computador}\33[m. Total de {soma} deu IMPAR")
        print("Computador venceu!")
        print(f"GAME OVER!!!Você derrotou o computador por {cont} rounds.")
        defeat.play()
        time.sleep(3)
        print("=*" * 30)
        break
    else:
        print(f"Você jogou \33[32m{jogador}\33[m e o computador jogou \33[31m{computador}\33[m. Total de {soma} deu PAR")
        print("Computador venceu!")
        print(f"GAME OVER!!!Você derrotou o computador por \33[1m\33[34m{cont}\33[0m rounds.")
        defeat.play()
        time.sleep(3)
        print("=*" * 30)
        break
    print("Vamos jogar novamente...")
    print("=*" * 30)
