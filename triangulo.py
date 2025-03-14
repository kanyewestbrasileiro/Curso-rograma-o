n1 = int(input("escreva um número: "))
n2 = int(input("escreva outro número: "))
n3 = int(input("escreva o ultimo número: "))
if(n1 + n2>n3):
    print("é um triangulo")
elif(n1 + n2<n3):
    print("não é um triangulo")
elif(n3 + n2>n1):
    print("é um triangulo")
elif(n3 + n2<n1):
    print("não é um triangulo")
elif(n3 + n1>n2):
    print("é um triangulo")
elif(n3 + n1<n2):
    print("não é um triangulo")
