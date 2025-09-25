num=int(input("Digite um número:"))
print("A tabuada do número {}\n".format(num))
contador=0
while(contador<=10):
    print("\n{} X {}= {}".format(num,contador,num*contador))
    contador+=1