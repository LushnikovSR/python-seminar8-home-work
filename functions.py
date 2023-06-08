def show_data() -> None:
    """Выводит информацию из справочника"""
    print(read_file())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def show_find_data(text: str) -> None:
    """Выводит результат поиска по справочнику."""
    print(find_data())


def find_data() -> None:
    """Возвращает результат поиска по справочнику."""
    data = read_file()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    result = search(data, data_to_find)
    return result


def read_file() -> str:
    """Возвращает данные из файла."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    return data


def search(in_book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = in_book.split('\n')
    result_lt = list(filter(lambda contact: contact if info in contact
                            else False, book))
    if len(result_lt) == 0:
        print('Совпадений не найдено')
        clarify_info = input('Уточните данные для поиска: ')
        return search(in_book, clarify_info)
    elif len(result_lt) == 1:
        return result_lt[0]
    elif len(result_lt) > 1:
        print('Найдено несколько совпадений:')
        print(result_lt, sep=',')
        clarify_info = input('Уточните данные для поиска: ')
        return search(in_book, clarify_info)


def change_data() -> None:
    """Изменяет данные в отдельном контакте"""
    contact = find_data()
    print(contact)
    data_file = replace_data(read_file(), contact)
    with open('book.txt', 'r+', encoding='utf-8') as file:
        file.write(data_file)


def replace_data(data: str, old_info: str) -> str:
    """Заменяет старые данные на новые"""
    print('введите: 1 - изменить фио, 2 - изменить номер телефона')
    mode = int(input())
    if mode == 1:
        new_info = input('Введите новые фио для изменения контакта: ')
        data = data.replace(old_info.split(' | ')[0],
                            new_info)
    elif mode == 2:
        new_info = input('Введите новый номер для изменения контакта: ')
        data = data.replace(old_info.split(' | ')[1],
                            new_info)
    else:
        replace_data(data, old_info)
    return data


def delete_data() -> None:
    """Удаляет данные по определенному критерию поиска"""
    contact = find_data()
    print(contact)
    with open('book.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
        file_content = [line.rstrip() for line in file_lines
                        if contact not in line]
        new_file_content = '\n'.join(file_content)
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write(new_file_content)
