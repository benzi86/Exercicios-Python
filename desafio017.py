from math import hypot
catop=float(input("Digite o comprimento do cateto oposto:"))
catad=float(input("Digite o comprimento do cateto adjacente:"))
print("O comprimento da hipotenusa é: {:.5}".format(hypot(catop,catad)))

