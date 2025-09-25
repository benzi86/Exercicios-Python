print("=*="*18)
print("Calculo IMC".center(52))
print("=*="*18)
peso=float(input("Digite seu peso em Kg: "))
alt=float(input("Digite sua altura em (metros): "))
imc=peso/(alt**2)
if imc<18.5:
    print("Você está abaixo do peso! Seu IMC é {:.1f}".format(imc))
elif imc>=18.5 and imc<25:
    print("Você está no peso ideal! Seu IMC é {:.1f}".format(imc))
elif imc>=25 and imc<30:
    print("Você está com sobrepeso! Seu IMC é {:.1f}".format(imc))
elif imc>=30 and imc<40:
    print("Você está com obesidade!Cuidado seu IMC é {:.1f}".format(imc))
else:
    print("Obesidade Mórbida, procure um médico e cuide de sua saúde! Seu IMC é {:.1f}".format(imc))
