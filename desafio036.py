print("\33[0;31m-=-"*18)
print("\33[1;33mSimulador compra de Casas")
print("\33[0;31m-=-\33[0m"*18)
valor_casa=float(input("Digite o valor da casa: R$"))
sal=float(input("Digite o valor de seu salário bruto atual: R$"))
par=int(input("Quantos anos de financiamento? "))
taxa=float(0.30)
prest_mensal=valor_casa/(par*12)
perc=prest_mensal/sal
print("Para pagar uma casa no valor de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}, representando {:.0%} do seu salário".format(valor_casa,par,prest_mensal,perc))
if perc>taxa:
    print("Financiamento negado!")
elif perc<=taxa:
    print("Financiamento aprovado!")
