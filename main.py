path = 'tel.txt'


def main_menu():
    while True:
        answer = (input('''Введите запрос:
        1. Открыть файл телефонной книги 
        2. Сохранить телефонную книгу 
        3. Показать все контакты
        4. Найти контакт
        5. Добавить контакт
        6. Изменить контакт 
        7. Удалить контакт
        8. Выход 
    :'''))

        if answer.isdigit() and 1 <= int(answer) <= 8:
            answer = int(answer)
            match answer:
                case 1:
                    pb = open_file()
                    print("Файл открыт")
                case 2:
                    save_file(pb)
                case 3:
                    if not pb:
                        print('Файл телефонной книги не существует или не открыт')
                    else:
                        show_phone_book(pb)
                case 4:
                    search_contact(pb)
                case 5:
                    pb.append(add_contact())
                    print('Контакт добавлен')
                case 6:
                    pb = change_contact(pb)
                    print('Контакт изменён')
                case 7:
                    pb = delete_contact(pb)
                    print('Контакт удалён')
                case 8:
                    print('До свидания')
                    break
        else:
            print('Введите число от 1 до 8')


def open_file():
    phone_book = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(':')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)
    return phone_book


def show_phone_book(pb: list[dict]):
    for i, contact in enumerate(pb, 1):
        print(f'{i}. {contact.get("name"): <20} '
              f'{contact.get("phone"): <20} '
              f'{contact.get("comment"): <20}')


def search_contact(phone_book: list[dict]):
    search = input('Введите данные для поиска: ').lower()
    count = 0
    for i, contact in enumerate(phone_book, 1):
        if search in f'{i}. {contact.get("name")}{contact.get("phone")}{contact.get("comment")}'.lower():
            print(f'{i}. {contact.get("name"): <20} '
                  f'{contact.get("phone"): <20} '
                  f'{contact.get("comment"): <20}')
            count += 1
    if count == 0:
        print('Ничего не нашлось')


def add_contact():
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    contact = {'name': name, 'phone': phone, 'comment': comment}
    return contact


def change_contact(book: list[{dict}]):
    index = int(input('Введите индекс изменяемого контакта: '))
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    renew_contact = {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}
    book.pop(index - 1)
    book.insert(index - 1, renew_contact)
    return book


def delete_contact(book: list[{dict}]):
    index = int(input('Введите индекс удаляемого контакта: '))
    book.pop(index - 1)
    return book


def save_file(book):
    data = []
    for contact in book:
        data.append(':'.join(list(contact.values())))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


main_menu()




