print("=*="*18)
print("{:=^40}".format("Compras Online"))
print("=*="*18)
compra=float(input("Digite o valor da sua compra:"))
print("Selecione a forma de pagamento")
print("[1]Dinheiro ou Cheque")
print("[2]Cartão de crédito a vista")
print("[3]Parcelado 2x no cartão de crédito")
print("[4]Parcelado 3x ou mais cartão de crédito")
cod=int(input("Digite o código referente a sua forma de pagamento:"))
if cod==1:
    pag=compra-(compra*0.1)
    print("Sua compra de R${:.2f} reais teve um desconto de 10%, preço final: R${:.2f} reais".format(compra,pag))
elif cod==2:
    pag=compra-(compra*0.05)
    print("Sua compra de R${:.2f} reais teve um desconto de 5%, preço final: R${:.2f} reais".format(compra, pag))
elif cod==3:
    par=compra/2
    print("Sua compra foi no valor de R${:.2f} reais, e será parcelada em 2X de R${:.2f} reais".format(compra,par))
elif cod==4:
    par=int(input("Digite a quantidade de parcelas:"))
    if par>2:
        compra_par=compra//par
        print("Sua compra será parcelada em {}X de R${:.2f} reais".format(par,compra_par))
        pag=compra+(compra*0.2)
        print("Sua compra foi no valor de R${:.2f} reais com acréscimo de 20% de juros, preço final de {:.2f} reais".format(compra,pag))
    else:
        print("Quantidade de parcelas não aceitas para esta opção, insira a opção [3] para continuar com o pagamento em 2X ou [2] para pagamento a vista.")
else:
    print("O código  selecionado é inválido, insira os dados novamente para continuar com o pagamento.")
