print("Sequência de Fibonacci")
num=int(input("Digite quantos termos quer mostrar: "))
cont=2
soma=0
n1=0
n2=1
print("{}→ {}→ ".format(n1,n2), end="")
while cont<num:
    soma = n1 + n2
    print("{}".format(soma), end="→ ")
    n1=n2
    n2=soma
    cont+=1
print("fim")
