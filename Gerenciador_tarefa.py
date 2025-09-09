# Gerenciador de tarefas simples no terminal
# Aqui o usuário pode adicionar, listar e remover tarefas

# Lista onde vamos guardar as tarefas
tarefas = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

# Loop principal do programa
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        # Adiciona uma nova tarefa
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print(" Tarefa adicionada!")

    elif escolha == "2":
        # Lista todas as tarefas
        if len(tarefas) == 0:
            print("Nenhuma tarefa adicionada ainda.")
        else:
            print("\n📋 Suas tarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")

    elif escolha == "3":
        # Remove uma tarefa pelo número
        if len(tarefas) == 0:
            print(" Não há tarefas para remover.")
        else:
            print("\nQual tarefa você quer remover?")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
            try:
                indice = int(input("Digite o número da tarefa: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f" Tarefa '{removida}' removida!")
                else:
                    print( "Número inválido.")
            except ValueError:
                print(" Por favor, digite um número válido.")

    elif escolha == "4":
        # Sai do programa
        print(" Saindo... Até mais!")
        break

    else:
        print(" Opção inválida. Tente novamente.")
