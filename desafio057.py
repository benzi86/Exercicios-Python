print("Informe o sexo (M/F) dos candidatos, para encerrar o programa digite 0(zero)")
sexo=input("Digite o sexo [F/M]:").strip().upper()[0]
while sexo not in 'MF':
    sexo=input("\33[31mDigite o valor  correto para o sexo [F/M]:\33[m").strip().upper()[0]
print("\33[32mRegistro do sexo {} realizado com sucesso!\33[m".format(sexo))




