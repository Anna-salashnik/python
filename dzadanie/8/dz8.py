def find_word_position(text, word):
    text_lower = text.lower()
    word_lower = word.lower()
    
    if word_lower in text_lower:
        position = text_lower.index(word_lower)
        print(f"Слово '{word}' найдено в тексте. Начинается с позиции: {position}")
    else:
        print(f"Слово '{word}' не найдено в тексте.")

# Получаем текст от пользователя
user_text = input("Введите текст: ")
# Запрашиваем слово, которое нужно найти в тексте
search_word = input("Введите слово для поиска: ")

# Определяем позицию слова в тексте (если оно есть)
find_word_position(user_text, search_word)
