idade = int(input("qual é sua idade?: "))
if(idade >=18) and (idade<60):
    print("adulto")
elif(idade<18):
    print("menor de idade")
elif(idade>=60):
    print("idoso")