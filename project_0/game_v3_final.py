def game_core_v3(number: int = 1) -> int:
    """Угадываем число путем нахождения середины от допустимого диапазона чисел.
    Допустимый диапазон на каждом этапе этерации сокращаем в двое в зависимости
    от полученного ответа: больше или меньше задуманное число от предсказанного

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    # Для первой этерации границы допустимого диапазона назначаем  как 1 и 100,
    #     а предсказанное значение как 50
    min_number, max_number = 1, 100
    predict = 50
  
    while True:
        count += 1
        if number == predict: break
        if number < predict:
            max_number = predict # Уменьшаем верхнюю границу
            predict = (min_number+max_number) // 2 # При доробном делении округляем вниз
        elif number > predict:
            min_number = predict # Увеличиваем нижнюю границу
            n = 0 if (min_number+max_number) % 2 == 0 else 1
            predict = (min_number+max_number)//2 + n # При дробном делении округляем вверх
                
    return count