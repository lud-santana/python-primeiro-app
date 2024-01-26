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
    linha = "*" * (len(texto) + 3)
    print(linha, "\n")
    print("* " + texto + " *", "\n")
    print(linha, "\n")

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
    
    print("Nome".ljust(22), "Categoria".ljust(22), "Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        
        print(f"\n- {nome_restaurante.ljust(20)} - {categoria_restaurante.ljust(20)} - {ativo}", "\n", "-" * 65)
    
    retornar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante cujo estado deve ser alterado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"\nO restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"\nO restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante {} não foi encontrado".format(nome_restaurante))
    
    retornar_ao_menu_principal()

def exibir_nome_do_app():
    print("""
    < 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 >            
    """)

def exibir_opcoes():
    print("""
        1. Cadastrar restaurante
        2. Listar restaurantes
        3. Alternar estado de restaurantes
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
                alternar_estado_restaurante()

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