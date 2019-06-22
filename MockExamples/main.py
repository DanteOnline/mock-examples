from lib import my_function
import os


def base_func():
    # Вызов функции из нашего модуля
    print('функция из нашего модуля венрнула', my_function())
    print('2-ой раз', my_function())
    # Вызов функции из стороннего модуля
    print('os:', os.getcwd())


if __name__ == '__main__':
    base_func()
