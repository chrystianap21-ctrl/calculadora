import math
import sys


def get_float(prompt, allow_negative=True):
    while True:
        try:
            value = float(input(prompt).strip())
            if not allow_negative and value < 0:
                print("Entrada inválida. Digite um número não negativo.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def get_int(prompt, valid_options=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if valid_options and value not in valid_options:
                print(f"Opção inválida. Escolha uma das opções: {valid_options}")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


def soma():
    a = get_float("Digite o primeiro número: ")
    b = get_float("Digite o segundo número: ")
    print(f"Resultado: {a} + {b} = {a + b}")


def subtracao():
    a = get_float("Digite o minuendo: ")
    b = get_float("Digite o subtraendo: ")
    print(f"Resultado: {a} - {b} = {a - b}")


def multiplicacao():
    a = get_float("Digite o primeiro número: ")
    b = get_float("Digite o segundo número: ")
    print(f"Resultado: {a} × {b} = {a * b}")


def divisao():
    a = get_float("Digite o dividendo: ")
    b = get_float("Digite o divisor: ")
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    else:
        print(f"Resultado: {a} ÷ {b} = {resultado}")


def potencia():
    a = get_float("Digite a base: ")
    b = get_float("Digite o expoente: ")
    try:
        resultado = math.pow(a, b)
    except OverflowError:
        print("Erro: resultado muito grande para ser calculado.")
    else:
        print(f"Resultado: {a} ^ {b} = {resultado}")


def raiz_quadrada():
    a = get_float("Digite o número para calcular a raiz quadrada: ", allow_negative=False)
    resultado = math.sqrt(a)
    print(f"Resultado: √{a} = {resultado}")


def logaritmo():
    a = get_float("Digite o número para calcular o logaritmo: ", allow_negative=False)
    print("Escolha o tipo de logaritmo:")
    print("1) ln")
    print("2) log10")
    print("3) log base personalizada")
    opcao = get_int("Opção: ", valid_options={1, 2, 3})

    if opcao == 1:
        resultado = math.log(a)
        print(f"Resultado: ln({a}) = {resultado}")
    elif opcao == 2:
        resultado = math.log10(a)
        print(f"Resultado: log10({a}) = {resultado}")
    else:
        base = get_float("Digite a base (diferente de 1): ")
        if base == 1:
            print("Erro: a base do logaritmo não pode ser 1.")
            return
        resultado = math.log(a, base)
        print(f"Resultado: log base {base} de {a} = {resultado}")


def trigonometria():
    print("Escolha a função trigonométrica:")
    print("1) seno")
    print("2) cosseno")
    print("3) tangente")
    opcao = get_int("Opção: ", valid_options={1, 2, 3})

    print("Escolha a unidade de ângulo:")
    print("1) Graus")
    print("2) Radianos")
    unidade = get_int("Unidade: ", valid_options={1, 2})

    angulo = get_float("Digite o valor do ângulo: ")
    if unidade == 1:
        angulo = math.radians(angulo)

    if opcao == 1:
        resultado = math.sin(angulo)
        func = "sen"
    elif opcao == 2:
        resultado = math.cos(angulo)
        func = "cos"
    else:
        if math.isclose(math.cos(angulo), 0.0, abs_tol=1e-12):
            print("Erro: tangente indefinida para este ângulo.")
            return
        resultado = math.tan(angulo)
        func = "tan"

    print(f"Resultado: {func}({angulo}) = {resultado}")


def exibir_menu():
    print("\n=== Calculadora Científica ===")
    print("1) Soma")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("5) Potência")
    print("6) Raiz quadrada")
    print("7) Logaritmo")
    print("8) Trigonometria")
    print("9) Sair")


def main():
    operacoes = {
        1: soma,
        2: subtracao,
        3: multiplicacao,
        4: divisao,
        5: potencia,
        6: raiz_quadrada,
        7: logaritmo,
        8: trigonometria,
    }

    while True:
        exibir_menu()
        escolha = get_int("Escolha uma operação: ", valid_options=set(range(1, 10)))

        if escolha == 9:
            print("Encerrando a calculadora. Até logo!")
            break

        operacao = operacoes.get(escolha)
        if operacao:
            operacao()
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        sys.exit(0)
