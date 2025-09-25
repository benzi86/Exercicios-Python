import math
ang= float(input("Digite o valor do ângulo:"))
ang_rad=math.radians(ang)
print("\nO valor do =>Cosseno é: {:.2}, o valor do =>Seno é {:.2} e o valor da =>Tangente é:{:.2}".format(math.cos(ang_rad),math.sin(ang_rad),math.tan(ang_rad)))