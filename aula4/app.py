import os

restaurantes = [
    {"nome": "Junin das Arábias", "categoria": "Árabe", "ativo": False}, 
    {"nome": "Carlos do Peixe", "categoria": "Japonesa", "ativo": True},
    {"nome": "Pizza da braba", "categoria": "Italiana", "ativo": False}
    ]

def retornar_ao_menu_principal():
    input("\nDigite uma tecla para retornar ao menu principal: ")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto, "\n")

def cadastrar_novo_restaurante():
    exibir_subtitulo("𝐶𝑎𝑑𝑎𝑠𝑡𝑟𝑜 𝑑𝑒 𝑅𝑒𝑠𝑡𝑎𝑢𝑟𝑎𝑛𝑡𝑒𝑠")

    nome_do_restaurante = input("- Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"- Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria_restaurante,
        "ativo": False
    }
    restaurantes.append(dados_do_restaurante)

    print("\nO restaurante {} foi cadastrado com sucesso!\n".format(nome_do_restaurante))
    retornar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("𝐿𝑖𝑠𝑡𝑎𝑛𝑑𝑜 𝑟𝑒𝑠𝑡𝑎𝑢𝑟𝑎𝑛𝑡𝑒𝑠")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        status_restaurante = restaurante["ativo"]
        
        print(f"\n- {nome_restaurante}\n- {categoria_restaurante}\n- {status_restaurante}\n_____________________")
    
    retornar_ao_menu_principal()

def ativar_restaurantes():
    pass

def exibir_nome_do_app():
    print("""
    < 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 >            
    """)

def exibir_opcoes():
    print("""
        1. Cadastrar restaurante
        2. Listar restaurantes
        3. Ativar restaurantes
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
    exibir_subtitulo("𝐹𝑖𝑛𝑎𝑙𝑖𝑧𝑎𝑛𝑑𝑜 𝐴𝑝𝑝...")

def opcao_invalida():
    print("Opção inválida!\n\n")
    retornar_ao_menu_principal()

def main():
    os.system("cls")

    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

    

if __name__ == "__main__":
    main()