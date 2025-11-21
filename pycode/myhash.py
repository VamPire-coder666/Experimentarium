from hashlib import sha256
from sqlite3 import connect


def fhash(obj: str):
    """Функция для хэширования

    Args:
        obj (str): строка, которую надо хэшировать
    Returns:
        str: захешированная строка
    """
    
    # Создание объекта хэширования
    hasher = sha256()
    # Обновление объекта хэширования данными
    hasher.update(bytes(obj, encoding='utf-8'))
    # Получение хэша в шестнадцатеричном формате
    return hasher.hexdigest()


def count_of_users():
    """Функция для получения числа пользоватлей

    Returns:
        int: число пользователей
    """
    
    connection = connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    total = len(cursor.fetchall())
    connection.close()
    return total


def user_to_db(login, password, name, surname):
    """Добавление пользователя в БД

    Args:
        login (str): логин
        password (str): пароль
        name (str): имя
        surname (str): фамилия
    """
    
    connection = connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (id, login, password, name, surname) VALUES (?, ?, ?, ?, ?)',
                   (count_of_users(), login, fhash(password), name, surname))
    connection.commit()
    connection.close()