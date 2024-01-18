import os

restaurantes = ["Junin das Arábias", "Carlos do Peixe"]

def retorno_para_main():
    input("\nDigite uma tecla para retornar ao menu principal: ")
    main()

def cadastrar_novo_restaurante():
    os.system("cls")
    print("𝐶𝑎𝑑𝑎𝑠𝑡𝑟𝑜 𝑑𝑒 𝑛𝑜𝑣𝑜𝑠 𝑟𝑒𝑠𝑡𝑎𝑢𝑟𝑎𝑛𝑡𝑒𝑠 \n\n")

    nome_do_restaurante = input("- Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)

    print("\nO restaurante {} foi cadastrado com sucesso!\n".format(nome_do_restaurante))
    retorno_para_main()

def listar_restaurantes():
    os.system("cls")

    print("𝐿𝑖𝑠𝑡𝑎𝑛𝑑𝑜 𝑟𝑒𝑠𝑡𝑎𝑢𝑟𝑎𝑛𝑡𝑒𝑠\n")
    for restaurante in restaurantes:
        print(f"- {restaurante}")
    
    retorno_para_main()

def ativar_restaurantes():
    pass

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
                cadastrar_novo_restaurante()
                #print(f"Sua escolha foi {opcao_escolhida}.\n\n Cadastrando restaurante...\n")
            
            case 2:
                listar_restaurantes()
            
            case 3:
                ativar_restaurantes()

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
    print("Finalizando app...\n\n")

def opcao_invalida():
    print("Opção inválida!\n\n")
    retorno_para_main()

def main():
    os.system("cls")

    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

    

if __name__ == "__main__":
    main()