def send_email(message, recipient, sender = "university.help@gmail.com"):

    # Проверка типа сообщения
    if isinstance(message, str):
        print("Строковый формат данных.")
    else:
        print("Нестроковый формат данных!")

    # Проверка корректности email-адресов
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка корректности получения и отправителя
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}! Введен некорректный email!")
        return

    # Провеяем, что отправитель не отправляет письмо самому себе
    if sender == recipient:
        print("Невозможно отправить письмо самому себе!")
        return

    # Прверка отправителя о умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")




# Примеры использования функций:
send_email("Добрый день!", "konfee88@yandex.ru")
print("---------------------------------------------------------------------------------------------------------------")
send_email("Добрый день!", "konfee88@yandex.ru", "maxales@gmail.com")
print("---------------------------------------------------------------------------------------------------------------")
send_email("Добрый день!", "konfee88@yandex.ru", "university.help@gmail.com")
print("---------------------------------------------------------------------------------------------------------------")
send_email("Добрый день!", "konfee88@yandex.ru", "konfee88@yandex.ru")
print("---------------------------------------------------------------------------------------------------------------")
send_email(4555654, "konfee88@yandex.ru", "konfee88@yandex.ru")
print("---------------------------------------------------------------------------------------------------------------")
send_email("Добрый день!", "konfee88@yandex", "konfee88yandex.ru")