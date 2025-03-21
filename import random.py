import random
quer_continuar = True
contador = 1
while(quer_continuar):
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    print(f"Q{+contador}{numero1}+{numero2}") 
    resp = int(input("R: "))
    if(resp == numero1+numero2):
        print("Resposta correta!")
    else:
        print("Resposta incorreta!")
    
contador = contador+1
quer_continuar = input("quer continuar? [1]sim [2] não")
if(quer_continuar == 2):
    quer_continuar = False

        
