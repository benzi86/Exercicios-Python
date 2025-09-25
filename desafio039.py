from datetime import date
print("\33[33m=*=\33[0m"*15)
print("Consulta de tempo para o 'Alistamento Militar'")
print("\33[33m=*=\33[0m"*15)
ano=int(input("Digite o ano de nascimento: "))
ano_atual=date.today().year
idade=ano_atual-ano
print("Quem nasceu no ano de {} atualmente tem {} anos!".format(ano,idade))
if idade==17:
    print("Ainda falta {} ano para o seu alistamento".format(18-idade))
elif idade<18:
    print("Ainda faltam {} anos para o seu alistamento".format(18-idade))
    print("Seu alistamento será no ano de {}".format(ano_atual+(18-idade)))
elif idade>18 and idade<=65:
    print("Você já passou da hora de se alistar, seu alistamento foi no ano de {}!".format(ano_atual+(18-idade)))
elif idade==18:
    print("Seu ano de alistamento é {}!!! Aliste-se já!".format(ano_atual))
else:
    print("Você passou dos 65 anos não será convocado! Aproveite sua aposentadoria...")

