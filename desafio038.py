num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
if num2>num1:
    maior=num2
    print("O segundo valor {} é maior que o primeiro valor {}".format(maior,num1))
elif num2<num1:
    maior=num1
    print("O primeiro valor {} é maior que o segundo valor {}".format(maior,num2))
elif num1==num2:
    print("Os valores são iguais!")
