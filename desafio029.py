vel=float(input("Digite a velocidade atual de seu carro:"))
if vel>80:
    multa=(vel-80)*7
    print("\33[1;33mAtenção você foi multado! O limite é de \33[1;31m80KM/H\33[1;33m, a multa aplicada foi de R${:.2f} reais".format(multa))
    print("\033[0;32mTenha um bom dia!Segurança em primeiro lugar.")
else:
    print("Dentro do limite permitido, tenha um bom dia!")
