num= str(input("Digite um número de 0 até 9999:"))
if num<'0' or num>'9999':
    print('Número invalído, digite um número entre 0 e 9999:')
print("unidade:",num[3])
print("dezena:",num[2])
print("centena:",num[1])
print("milhar:",num[0])
