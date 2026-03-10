while True:
    print("\n===Gerenciador de Tarefas===")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif op == "2":
        print("\nTarefas:")
        if not tarefas:
            print("Nenhuma tarefa adicionada ainda.")
        else:
            for i, t in enumerate(tarefas):
                print(f"{i+1} - {t}") # Corrected print statement

    elif op == "3": # Corrected 'opcao' to 'op'
        num_str = input("Número da tarefa para remover: ")
        if num_str.isdigit():
            num = int(num_str) - 1 # Adjust for 0-based indexing
            if 0 <= num < len(tarefas):
                tarefas.pop(num)
                print("Tarefa removida!")
            else:
                print("Número inválido!")
        else:
            print("Entrada inválida. Por favor, digite um número.")

    elif op == "4": # Corrected 'opcao' to 'op'
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
