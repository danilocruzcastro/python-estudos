while True:
    print("\n=====CALCULADORA=====")

    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))

    print("\nEscolha a opção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    op = input("Escolha:")
    if op == "1":
        resultado = num1 + num2
        print("Resultado: ", resultado)

    elif op == "2":
        resultado = num1 - num2
        print("Resultado: ", resultado)

    elif op == "3":
        resultado = num1 * num2
        print("Resultado: ", resultado)

    elif op =="4":
      if num2 !=0:
        resultado = num1 / num2
        print("Resultado:", resultado)
      else:
        print("Erro: Divisão por zero!")
    else: # Este 'else' agora pertence corretamente à cadeia 'if/elif op'
      print("Opção invalida")

    continuar = input("\nDeseja fazer outra conta? (s/n): ") # Chamada da função input corrigida
    if continuar.lower() !="s":
      print("Encerrando calculadora...")
      break
