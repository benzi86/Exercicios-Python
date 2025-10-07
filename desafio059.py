from time import sleep
choice=0
num1=int(input("Digite o 1º número: "))
num2=int(input("Digite o 2º número: "))
while choice!= 5:
    sleep(1)
    print(""" [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Sair do programa""")
    choice = int(input("=>Digite sua opção:"))
    if choice == 1:
        soma=num1+num2
        print("A soma dos números {} + {} = {}".format(num1, num2, soma))
    elif choice == 2:
        multiplicar=num1*num2
        print("A multiplicação entre os números {} X {} = {}".format(num1, num2, multiplicar))
    elif choice == 3:
        if num1 > num2:
            maior=num1
        else:
            maior=num2
        print("Entre {} e {} o maior valor é {}".format(num1, num2, maior))
    elif choice == 4:
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))
    elif choice == 5:
        print("Obrigado por usar o programa!")
        sleep(1)
    else:
        print("Opção invalida! Digite novamente")
print("Fim do programa!")




