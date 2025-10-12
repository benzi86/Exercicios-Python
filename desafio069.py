print("Cadastro Pessoal")
idade= i= m= f= cont= 0
sexo= validar= ""
while True:
    idade=int(input("Digite sua idade: "))
    if idade>=18:
        i+=1
    sexo=str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
    if sexo == "M":
        m += 1
    elif sexo == "F" and idade < 20:
        f += 1
    while sexo not in "MF":
        sexo = str(input("Digite uma opção válida [M] para Masculino e [F] para Feminino: ")).upper().strip()[0]
    validar=str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    while validar not in "SN":
        validar = str(input("Digite uma opção válida [S] para continuar ou [N] para encerrar: ")).upper().strip()[0]
    if validar == "N":
        break
print(f"Foram cadastradas \33[32m{i}\33[0m pessoas com mais de 18 anos.")
print(f"Foram registrados \33[34m{m}\33[0m homens e \33[35m{f}\33[0m mulheres com menos de 20 anos")
