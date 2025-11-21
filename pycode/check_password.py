import re

def check_password(password):
    """ The function checks the correctness of the password

    Args:
        password (str): password, that need to be checked

    Returns:
        bool: password correct or incorrect
        str/None: the problem of the password or None if password is correct
    """
    if len(password) < 8:
        return False, "Пароль должен содержать минимум 8 символов"
    if not re.search(r'[A-Z]', password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    if not re.search(r'[a-z]', password):
        return False, "Пароль должен содержать хотя бы одну строчную букву"
    if not re.search(r'\d', password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    if not re.search(r'[!@#$%^&*()\-_+=]', password):
        return False, "Пароль должен содержать хотя бы один специальный символ"
    return True, None