import numpy as np

def random_predict(number: int) -> int:
    """Функция для угадывания числа с использованием бинарного поиска."""
    count = 0
    low = 1
    high = 100
    predict = (low + high) // 2  # Начальное предположение

    while predict != number:
        count += 1
        if predict < number:
            low = predict + 1  # Увеличиваем нижнюю границу
        elif predict > number:
            high = predict - 1  # Уменьшаем верхнюю границу
        predict = (low + high) // 2  # Угадываем новое среднее значение

    return count  # Возвращаем количество попыток

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм."""
    count_ls = []  # Список для сохранения количества попыток
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))  # Считаем попытки для каждого числа

    score = int(np.mean(count_ls))  # Находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# Запускаем игру
score_game(random_predict)
