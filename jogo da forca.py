roblox_2_é_real = ["leite", "cafe", "merda enlatada"]
while True:
        print("[1] Cadastrar produto")
        print("[2] remover produto")
        print("[3] Alterar nome do produto")
        print("[4] ver todos os produtos")
        print("[5] sair do programa porno")
        resposta = int (input("Qual o bixa deseja: "))
        if(resposta == 1):
                Novo_produto = (input("Digite o nome do produto"))
                roblox_2_é_real.append(Novo_produto)
        elif (resposta == 2):
                remover_produto = (input(f"Qual produto desejas remover? \n{roblox_2_é_real}"))
                roblox_2_é_real.remove(remover_produto)
        elif (resposta == 3):
                numero = 0
                for a in roblox_2_é_real:
                        print(f"produto: {a} -- opcão:{numero}")
                        numero += 1
                troca_troca = int (input(f"Qual produto voce deseja alterar o nome?: \n{roblox_2_é_real}"))
                roblox_2_é_real [troca_troca] = str (input("qual nome voce quer para esse produto?: "))        
        elif (resposta == 4):
                print(roblox_2_é_real)
        elif (resposta == 5):
                break
print(("fim 👉👌"))