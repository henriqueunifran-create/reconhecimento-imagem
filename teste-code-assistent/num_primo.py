def is_prime(n):
    """Verifica se um número inteiro é primo.

    Args:
        n (int): Número inteiro a ser verificado.

    Returns:
        bool: True se `n` for primo, False caso contrário.

    Notes:
        - Números menores ou iguais a 1 não são considerados primos.
        - Esta função usa teste otimizado, verificando divisibilidade por 2 e 3
          e, em seguida, por valores da forma 6k ± 1.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    try:
        value = int(input("Digite um número inteiro para verificar se é primo: "))
    except ValueError:
        print("Erro: digite um número inteiro válido.")
    else:
        if is_prime(value):
            print(f"{value} é primo.")
        else:
            print(f"{value} não é primo.")