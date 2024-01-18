import os

def exibir_nome_do_app():
    print("""
    < 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 >            
    """)

def exibir_opcoes():
    print("""
        1. Cadastrar restaurante
        2. Listar restaurante
        3. Ativar restaurante
        4. Sair
    """)
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                print(f"Sua escolha foi {opcao_escolhida}.\n\n Cadastrando restaurante...\n")
            
            case 2:
                print(f"Sua escolha foi {opcao_escolhida}.\n\n listando restaurante...\n")
            
            case 3:
                print(f"Sua escolha foi {opcao_escolhida}.\n\n Ativando restaurante...\n")
            case 4:
                encerrar_app()

            case __:
                opcao_invalida()
    
    except:
        opcao_invalida()

""" utilizando Match como alternativa para o bloco de if/elif/else abaixo
if opcao_escolhida == 1:
    print(f"Sua escolha foi {opcao_escolhida}.\n\n Cadastrando restaurante...\n")

elif opcao_escolhida == 2:
    print(f"Sua escolha foi {opcao_escolhida}.\n\n listando restaurante...\n")

elif opcao_escolhida == 3:
    print(f"Sua escolha foi {opcao_escolhida}.\n\n Ativando restaurante...\n")

elif opcao_escolhida == 4:
    encerrar_app()

else:
    print("Opção inválida!")"""

def encerrar_app():
    os.system("cls")
    print("Finalizando app...")

def opcao_invalida():
    print("Opção inválida!\n\n")
    input("Digite uma tecla para retornar ao menu principal: ")
    main()

def main():
    os.system("cls")

    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

    

if __name__ == "__main__":
    main()