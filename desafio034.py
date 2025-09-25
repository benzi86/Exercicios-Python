sal=float(input("Digite seu o valor de seu salário>:"))
perc1=float(0.10)
perc2=float(0.15)
if sal>=1250:
    novo_sal=sal+(sal*perc1)
    print("O salário com {:.0%} de aumento é de: {:.2f}".format(perc1,novo_sal))
else:
    novo_sal=sal+(sal*perc2)
    print("O salário com {:.0%} de aumento é de: {:.2f}".format(perc2,novo_sal))

