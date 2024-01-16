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
      opcao_escolhida = int(input("Escolha uma opção: "))

      if opcao_escolhida == 1:
            print(f"Sua escolha foi {opcao_escolhida}.\n\n Cadastrando restaurante...\n")

      elif opcao_escolhida == 2:
            print(f"Sua escolha foi {opcao_escolhida}.\n\n listando restaurante...\n")

      elif opcao_escolhida == 3:
            print(f"Sua escolha foi {opcao_escolhida}.\n\n Ativando restaurante...\n")

      else:
            encerrar_app()

def encerrar_app():
     os.system("cls")
     print("Finalizando app...")

def main():
      exibir_nome_do_app()
      exibir_opcoes()
      escolher_opcao()

      

if __name__ == "__main__":
      main()