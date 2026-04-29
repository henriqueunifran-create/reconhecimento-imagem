def is_prime(n):
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