def adição(x, y):
    return x + y

def subtração(x, y):
    return x - y

def multiplicação(x, y):
    return x * y

def divisão(x, y):
    if y == 0:
        return "Erro! Não foi possível dividir por zero."
    else:
        return x / y

while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Finalizar")

    escolha = input("Digite o número desejado: ")

    if escolha == '5':
        print("Obrigado por usar a calculadora. Até mais!")
        break
    elif escolha in ['1', '2', '3', '4']:
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", adição(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtração(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicação(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisão(num1, num2))
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 5.")
                          
