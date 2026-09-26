def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Факториал не определяется для отрицательных чисел")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result
