def say_hello():  
    print('Hello, World!')





def factorial():
    if n == 0:
    return 1
    else:
    return n * factorial(n-1)


def factorial():
    if n == 0:
    return 1
    else:
    return n * factorial(n-1)


def is_palindrome():
    def is_palindrome(s): return s.lower().replace(' ', '') == s.lower().replace(' ', '')[::-1]


def add_numbers():
    def add_numbers(a, b):
    return a + b


def factorial():
    def factorial(n):
    if n == 0 or n == 1:
    return 1
    else:
    result = 1
    for i in range(2, n + 1):
    result *= i
    return result


def open_calculator():
    import os
    
    def open_calculator():
    os.system('calc')
    return 'Calculator opened.'


def get_current_date_time(n):
    from datetime import datetime
    
    def get_current_date_time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_current_datetime(n):
    import datetime
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


def open_notepad(n):
    import os
    os.system('notepad')
