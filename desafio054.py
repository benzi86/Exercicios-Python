from datetime import date
print(str("Confira, você é maior de idade?"))
print("=*="*10)
data_atual=date.today()
maior=0
menor=0
for pessoa in range (1,8):
   ano=int(input("Digite o ano de nascimento da {} pessoa: ".format(pessoa)))
   idade=date.today().year - ano
   if idade >= 21:
       maior=maior+1
   else:
       menor=menor+1
print("Temos ao todo \033[32m{} \33[mpessoas maiores de idade".format(maior),end=" ")
print("e as pessoas menores de idade totalizam \33[31m{}\33[m".format(menor))

