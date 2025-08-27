import tkinter as tk
janela = tk.Tk()
janela.title("Bem vindo viajante! ")

nome = str(input("qual o seu nome?: "))
historia = print("Que nome bonito! ")
import random
força = random.randint(1, 20)
velocidade = random.randint(1, 20)
inteligencia = random.randint(1,20)
carisma = random.randint(1, 20)

print("Seus status são: ")
status_força = print(f" força: 💪 {força} 💪")
status_velocidade = print(f" velocidade: 🏃 {velocidade} 🏃")
status_inteligencia = print(f" inteligencia: 🧠 {inteligencia} 🧠")
status_carisma = print(f" carisma: 😄 {carisma} 😄")


guerreiro = 2
latino = 2
mago = 2
bardo = 2

classe = print("qual é a sua classe?:")

if classe == 1:
    resultado1 = guerreiro + força
    print(f"seus status de força agora são 💪 {resultado1} 💪")
elif classe == 2:
    resultado2 = latino+ velocidade
    print(f"seus status de velocidade agora são 🏃 {resultado2} 🏃")
elif classe == 3:
    resultado3 = mago + inteligencia
    print(f"seus status de inteligência agora são 🧠 {resultado3} 🧠")
else:
    resultado4 = bardo + carisma
    print(f"seus status de carisma agora são 😄 {resultado4} 😄 ") 
