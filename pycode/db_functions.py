import sqlite3

users_template = '''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
login TEXT,
password TEXT,
name TEXT,
surname TEXT
)
'''

exp_template = '''
CREATE TABLE IF NOT EXISTS Experiments (
id INTEGER PRIMARY KEY,
login TEXT,
type TEXT,
name TEXT,
env TEXT,
figures TEXT,
comments TEXT
)
'''

database_templates = {
    'users': (users_template, 'Users'),
    'experiments': (exp_template, 'Experiments')
}


def users_from_db_to_txt():
    """ Переписывает всех пользователей из бд в текстовый файл """
    
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    data = cursor.fetchall()
    with open('data/users.csv', 'w', encoding='utf-8') as f:
        f.write('name;surname;login;password;id')
        for row in data:
            res = list(map(str, row))
            f.write('\n' + ';'.join(res))
    connection.close()


def get_logins() -> list[str]:
    """ Функция для получения всех логинов

    Returns:
        list[str]: список строк - все логины пользователей
    """
    
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT login FROM Users')
    logins = [x[0] for x in cursor.fetchall()]
    connection.close()
    return logins


def read_db_users() -> list[tuple]:
    """ Функция для получения всей инфы про всез пользователей

    Returns:
        list[tuple]: список кортежей - вся инфа про всех пользователей
    """
    
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    data = cursor.fetchall()
    connection.close()
    data = sorted([tuple(i) for i in data], key=lambda x: x[0])
    return data


def get_logins_passwords() -> dict:
    """ Функция для получения логинов и паролей

    Returns:
        dict: словарь логин-пароль
    """
    
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT login, password FROM Users')
    data = cursor.fetchall()
    connection.close()
    res = {}
    for user in data:
        res[user[0]] = user[1]
    return res


def rewrite_db(name: str):
    """ Функция удаляет всю инфу из БД

    Args:
        name (str): 'users' или 'experiments' - БД, которую надо очистить
    """
    
    template, table = database_templates[name]
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table}')
    cursor.execute(template)
    connection.commit()
    connection.close()


def get_experiments(login=None) -> list[str]:
    """ Функция для получения названий всех экспериментов
    по логину

    Args:
        login (str, optional): Логин, под которым создан эксперимент.
    Если аргумент не передан - выведутся все эксперименты. Defaults to None.

    Returns:
        list[str]: список названий
    """
    
    if login:
        req = f"""SELECT name FROM Experiments
        WHERE login = '{login}'"""
    else:
        req = 'SELECT name FROM Experiments'
    con = sqlite3.connect('data/experiments.db')
    cursor = con.cursor()
    cursor.execute(req)
    data = cursor.fetchall()
    con.close()
    return [i[0] for i in data]


def get_exp_numbers() -> list[int]:
    """ Функция для возврата всех id экспериментов

    Returns:
        list[int]: список id всех экспериментов
    """
    
    con = sqlite3.connect('data/experiments.db')
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Experiments')
    data = cursor.fetchall()
    con.close()
    return [i[0] for i in data]


def save_experiment(exp) -> tuple:
    """ Функция для сохранения эксперимента

    Args:
        exp (ExperimentWindow): окно эксперимента, который надо сохранить

    Returns:
        tuple: кортеж из двух элементов - bool (сохранено или нет)
    и строка (что вывести в сообщение пользователю)
    """
    
    login = exp.main_window.login
    name = exp.expname_lineEdit.text()
    if not name:
        return False, 'У эксперимента должно быть имя'
    env = exp.env_comboBox.currentText()
    figures = ','.join(exp.figures_textbrowser.toPlainText().split('\n'))
    if not figures:
        return False, "В эксперименте должны быть тела"
    comments = exp.comments_textEdit.toPlainText().replace('\n', '|n|')
    if not comments:
        comments = 'None'
    tp = exp.type
    if name in get_experiments():
        delete_experiment(exp)
        save_experiment(exp)
    else:
        con = sqlite3.connect('data/experiments.db')
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO Experiments (login, type, name, env, figures, comments) VALUES (?, ?, ?, ?, ?, ?)',
            (login, tp, name, env, figures, comments)
        )
        con.commit()
        con.close()
    return True, 'Сохранено'


def delete_experiment(exp):
    """ Удаление эксперимента """
    
    name = exp.expname_lineEdit.text()
    if name not in get_experiments():
        return
    con = sqlite3.connect('data/experiments.db')
    cursor = con.cursor()
    cursor.execute(f"""DELETE FROM Experiments WHERE name = '{name}' AND login = '{exp.main_window.login}'""")
    con.commit()
    con.close()


def get_experiment(name, login) -> tuple:
    """ Функция возвращает все параметры эксперимента

    Args:
        name (str): название эксперимента
        login (str): логин пользователя

    Returns:
        tuple: параметры эксперимента
    """
    
    con = sqlite3.connect('data/experiments.db')
    cursor = con.cursor()
    cursor.execute(f'''SELECT * FROM Experiments
                        WHERE name="{name}" AND login="{login}"''')
    data = list(cursor.fetchall())
    con.close()
    if not data:
        return ()
    return tuple(data[0])


def save_ballistic_exp(exp) -> tuple:
    """ Функция для сохранения эксперимента типа баллистика

    Args:
        exp (ExperimentWindow): окно эксперимента, который надо сохранить

    Returns:
        tuple: кортеж из двух элементов - bool (сохранено или нет)
    и строка (что вывести в сообщение пользователю)
    """
    
    login = exp.main_window.login
    name = exp.expname_lineEdit.text()
    if not name:
        return False, 'У эксперимента должно быть имя'
    env = exp.env_comboBox.currentText()
    figures = exp.figures_textbrowser.toHtml()
    if not figures:
        return False, "В эксперименте должны быть тела"
    comments = exp.comments_textEdit.toPlainText()
    if not comments:
        comments = 'None'
    tp = exp.type
    if name in get_experiments():
        delete_experiment(exp)
        save_ballistic_exp(exp)
    else:
        con = sqlite3.connect('data/experiments.db')
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO Experiments (login, type, name, env, figures, comments) VALUES (?, ?, ?, ?, ?, ?)',
            (login, tp, name, env, figures, comments)
        )
        con.commit()
        con.close()
    return True, 'Сохранено'