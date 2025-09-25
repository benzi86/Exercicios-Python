from datetime import date
print("+-"*20)
print("\33[1;31mAssociação de Natação Internacional\33[0m")
print("+-"*20)
ano=int(input("Digite o ano de nascimento: "))
ano_atual=date.today().year
idade=ano_atual-ano
if idade<=9:
    print("Sua idade é {} anos, categoria é Mirim!".format(idade))
elif idade>9 and idade<=14:
    print("Sua idade é {} anos, categoria é Infantil!".format(idade))
elif idade>14 and idade<=19:
    print("Sua idade é {} anos, categoria é Junior!".format(idade))
elif idade>19 and idade<=20:
    print("Sua idade é {} anos, categoria é Sênior!".format(idade))
else:
    print("Sua idade é {} anos, categoria é Master!".format(idade))