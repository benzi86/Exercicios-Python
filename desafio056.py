print("Analisando Pessoas")
nome=0
idade=0
sexo=0
media=0
somaidade=0
maior_idade=0
nome_velho=""
mulher_nova=0
for pessoa in range(1,5):
    if pessoa==1:
        print("**{}º pessoa**".format(pessoa))
        nome=str(input("Nome:".format(nome)))
        idade=int(input("Idade:".format(idade)))
        sexo=str(input("Sexo[M/F]:".format(sexo)))
    if pessoa==2:
        print("**{}º pessoa**".format(pessoa))
        nome=str(input("Nome:".format(nome)))
        idade=int(input("Idade:".format(idade)))
        sexo=str(input("Sexo[M/F]:".format(sexo)))
    if pessoa==3:
        print("**{}º pessoa**".format(pessoa))
        nome=str(input("Nome:".format(nome)))
        idade=int(input("Idade:".format(idade)))
        sexo=str(input("Sexo[M/F]:".format(sexo)))
    if pessoa==4:
        print("**{}º pessoa**".format(pessoa))
        nome=str(input("Nome:".format(nome)))
        idade=int(input("Idade:".format(idade)))
        sexo=str(input("Sexo[M/F]:".format(sexo)))
    somaidade+=idade
    if pessoa==1:
        maior_idade=idade
        nome_velho=nome
    else:
        if idade>maior_idade and sexo in "Mm":
            maior_idade=idade
            nome_velho=nome
        if sexo in "Ff" and idade<20:
            mulher_nova+=1
media=somaidade/4
print("A média de idade do grupo é de: {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maior_idade,nome_velho))
print("{} mulhere(s) com menos de 20 anos!".format(mulher_nova))
