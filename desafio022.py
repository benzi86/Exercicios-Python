nome= str(input("Digite seu nome completo: "))
print("Nome Maiusculo:",nome.upper())
print("Nome minusculo:",nome.lower())
print("Qtd letras sem contar espaços:",len(nome.replace(" ","")))
print("Qtd letras do primeiro nome:",len(nome.split()[0]))

