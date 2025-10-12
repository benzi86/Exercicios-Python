print("Loja Gaste bem")
nome= rotulo= conf= ""
preco= soma= pcont= menor= cont= 0
while True:
    nome=str(input("Nome do produto:"))
    preco=float(input("Preço do produto: R$ "))
    conf = str(input("Continuar a compra? [S/N]: ")).upper().strip()
    cont+=1
    soma+=preco
    if preco>=1000:
        pcont+=1
    if cont==1 or preco<menor:
        menor=preco
        rotulo=nome
    while conf not in "SN":
        conf = str(input("Continuar a compra? [S/N]: ")).upper().strip()
    if conf == "N":
        break
print(f"O total gasto foi R$ {soma:.2f} reais.")
print(f"Temos {pcont} custando acima de R$ 1.000,00 reais.")
print(f"O produto mais barato foi {rotulo} que custa R$ {menor:.2f} reais.")