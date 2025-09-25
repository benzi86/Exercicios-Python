from random import randint
from time import sleep
print("{:=^30}".format("Vamos jogar Jokenpô!"))
print("""Selecione sua opção:
[1] PEDRA
"[2] PAPEL
"[3] TESOURA""")
player=int(input("Qual será sua jogada?"))
comp=randint(1,3)
if player>3 or player<1:#Opção diferente das declaradas
    print("Essa opção não existe!")
else:
    print("JO..")#inicio animação jokenpo
    sleep(1)
    print("KEN....")
    sleep(1)
    print("PO!!!")
    sleep(1)
    if player==1 and comp==3:#jogador seleciona pedra
        print("=*="*10)
        print("Jogador jogou PEDRA")
        print("Computador jogou TESOURA")
        print("=*=" * 10)
        print("JOGADOR VENCEU!!!")
    elif player==1 and comp==2:#jogador seleciona papel
        print("=*=" * 10)
        print("Jogador jogou PEDRA")
        print("Computador jogou PAPEL")
        print("=*=" * 10)
        print("COMPUTADOR VENCEU!!!")
    elif player==2 and comp==3:
        print("=*=" * 10)
        print("Jogador jogou PAPEL")
        print("Computador jogou TESOURA")
        print("=*=" * 10)
        print("COMPUTADOR VENCEU!!!")
    elif player==2 and comp==1:
        print("=*=" * 10)
        print("Jogador jogou PAPEL")
        print("Computador jogou PEDRA")
        print("=*=" * 10)
        print("JOGADOR VENCEU!!!")
    elif player==3 and comp==2:
        print("=*=" * 10)
        print("Jogador jogou TESOURA")
        print("Computador jogou PAPEL")
        print("=*=" * 10)
        print("JOGADOR VENCEU!!!")
    elif player==3 and comp==1:
        print("=*=" * 10)
        print("Jogador jogou TESOURA")
        print("Computador jogou PEDRA ")
        print("=*=" * 10)
        print("COMPUTADOR VENCEU!!!")
    else:
        print("=*=" * 10)
        print("EMPATE!!!, JOGUE OUTRA VEZ!")
        print("=*=" * 10)


