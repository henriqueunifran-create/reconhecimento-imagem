# Explicação do código `num_primo.py`

Este arquivo mostra como verificar se um número inteiro é primo em Python e inclui alguns testes básicos para validar o funcionamento.

## O que é um número primo?

Um número primo é um número inteiro maior que 1 que só é divisível por 1 e por ele mesmo. Exemplos de números primos: 2, 3, 5, 7, 11.

## Função `is_prime(n)`

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Passo a passo

1. `if n <= 1:`
   - Números menores ou iguais a 1 não são primos.
   - Retorna `False` nesses casos.

2. `for i in range(2, int(n**0.5) + 1):`
   - Testa possíveis divisores de `n` começando em 2.
   - O laço vai até a raiz quadrada de `n` porque, se `n` tem um divisor maior que sua raiz quadrada, ele também terá um divisor menor.
   - Isso reduz a quantidade de verificações e torna a função mais eficiente.

3. `if n % i == 0:`
   - Verifica se `i` divide `n` sem resto.
   - Se for divisível, `n` não é primo e a função retorna `False`.

4. `return True`
   - Se nenhum divisor for encontrado no laço, `n` é primo.
   - Retorna `True`.

## Testes da função

O código também inclui testes simples para mostrar o resultado de `is_prime` em alguns valores:

```python
print("Testando a função is_prime:")
print(f"is_prime(2): {is_prime(2)}")  # Deve ser True
print(f"is_prime(3): {is_prime(3)}")  # Deve ser True
print(f"is_prime(4): {is_prime(4)}")  # Deve ser False
print(f"is_prime(17): {is_prime(17)}")  # Deve ser True
print(f"is_prime(18): {is_prime(18)}")  # Deve ser False
print(f"is_prime(1): {is_prime(1)}")  # Deve ser False
print(f"is_prime(0): {is_prime(0)}")  # Deve ser False
```

### O que cada teste representa

- `2` e `3` são primos, então a função deve retornar `True`.
- `4` e `18` não são primos, pois têm divisores além de 1 e eles mesmos.
- `1` e `0` não são primos, por definição.

## Como usar

Basta executar o arquivo `num_primo.py` com Python. Ele exibirá os resultados dos testes no console.

```bash
python num_primo.py
```

## Conclusão

A função `is_prime` é uma forma simples e eficiente de verificar primalidade para números inteiros positivos. Ela usa a técnica de testar divisores somente até a raiz quadrada do número, o que melhora o desempenho em comparação com verificar todos os valores até `n-1`.
