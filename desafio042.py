
lado1=float(input("Digite o valor da primeira reta: "))
lado2=float(input("Digite o valor da segunda reta: "))
lado3=float(input("Digite o valor da terceira reta: "))

#Verficar se as medidas digitadas pelo usuario são validas.
def triangulos(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return "Não é possivel formar um triângulo com valores nulos!"
    if a>=b+c or b>=c+a or c>=b+a:
        return "Com esses lados não é possivel formar um triângulo!"
#classificar o tipo de triângulo
    if a==b and b==c:
        return "Este é um Triângulo Equilátero!"#Todos os lados são iguais
    elif a==b or b==c or a==c:
        return "Este é um Triângulo Isósceles!"#Dois lados iguais e um diferente
    else:
        return "Este é um Trinângulo Escaleno!"#Todos os lados são diferentes

triangulo_tipo=triangulos(lado1, lado2, lado3)
print(triangulo_tipo)
