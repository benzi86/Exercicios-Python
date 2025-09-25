numero=int(input("Digite um número para conversão:"))
print("""Escolha a base de conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal""")
opcao=int(input("Digite sua opção:"))
if opcao==1:
    print("O número {} convertido para Binário é {}".format(numero,bin(numero)[2:]))
elif opcao==2:
    print("O número {} convertido para Octal é {}".format(numero,oct(numero)[2:]))
elif opcao==3:
    print("O número {} convertido para Hexadecimal é {}".format(numero,hex(numero)[2:]))
else:
    print("A opção selecionada não existe!")


