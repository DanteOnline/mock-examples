"""
Примеры моков для pytest
"""
import os
import main


def test_my_function(mocker):
    # 1. Замена функции в из нашего модуля
    mocker.patch('main.my_function', return_value='abc')
    # вызываем функцию которую проверяем
    main.base_func()

    # Функция мок должна быть вызвана 2 раза
    assert main.my_function.call_count == 2


def test_side_package_function(mocker):
    # 2. Замена функции из стороннего модуля
    mocker.patch('os.getcwd', return_value='abc')
    main.base_func()
    assert os.getcwd.call_count == 1

def test_my_class(mocker):
    # 3. Замена класса из нашего модуля
    pass

def test_side_package(mocker):
    # 4. Замена класса из стороннего модуля
    pass
