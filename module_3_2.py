def send_email(message, recipient, sender = "university.help@gmail.com"):
    flag = False
    if ('.com' in recipient or '.ru' in recipient or '.net' in recipient) and ('@' in recipient) and ('.com' in sender or '.ru' in sender or '.net' in sender) and ('@' in sender):
        flag = True
    if flag == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if recipient == sender and flag == True:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')