nome=str(input("Digite seu nome: "))
print("+-"*15)
print("Boletim Escolar de {}".format(nome))
print("+-"*15)
n1=float(input("Digite a nota do 1º Trimestre:"))
n2=float(input("Digite a nota do 2º Trimestre:"))
med=(n1+n2)/2
if med<5:
    print("Sua média foi {:.1f} você foi Reprovado!".format(med))
elif med>=5 and med<=6.9:
    print("Sua média foi {:.1f} você está de Recuperação!".format(med))
else:
    print("Sua média foi {:.1f}, Parabéns você foi aprovado!".format(med))



