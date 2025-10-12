print("=*"*20)
print("{:^20}".format("Banco Novo **Seja bem Vindo!**"))
print("=*"*20)
sacar=int(input("Digite o valor do saque: R$ "))
cedula=50
total=sacar
contcedulas=0
while True:
    if total>=cedula:
        total-=cedula
        contcedulas+=1
    else:
        if contcedulas>0:
            print(f"Contagem de notas {contcedulas} totalizando R$ {cedula:.2f} ")
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=2
        elif cedula==2:
            cedula=1
        contcedulas=0
        if total==0:
          break
print("=*"*20)
print("Volte sempre! Tenha um bom dia!")

