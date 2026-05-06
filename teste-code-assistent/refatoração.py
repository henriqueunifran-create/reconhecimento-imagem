from typing import Iterable, Tuple


def compute_statistics(values: Iterable[float]) -> Tuple[float, float, float, float]:
    """Calcula estatísticas básicas a partir de um iterável de números.

    Args:
        values (Iterable[float]): Sequência de valores numéricos.

    Returns:
        Tuple[float, float, float, float]: tupla contendo, respectivamente,
            o total, a média, o valor máximo e o valor mínimo.

    Raises:
        ValueError: se o iterável estiver vazio.
    """
    values_list = list(values)
    if not values_list:
        raise ValueError("The input list must contain at least one number.")

    total = sum(values_list)
    mean_value = total / len(values_list)
    maximum = max(values_list)
    minimum = min(values_list)

    return total, mean_value, maximum, minimum


if __name__ == "__main__":
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, mean_value, maximum, minimum = compute_statistics(numbers)

    print("total:", total)
    print("media:", mean_value)
    print("maior:", maximum)
    print("menor:", minimum)
