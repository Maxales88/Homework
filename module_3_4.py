def single_root_word(root_word, *other_words):
    same_words = []

    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем условие наличия слова в корневом слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words

# Примеры вызова функции
result1 = single_root_word('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_word('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

