import pytest
from average import Spiski


# Тестирование метода average
def test_average():
    list1 = [2, 4, 6]
    result = Spiski.average(list1)
    assert result == 4


# Тестирование метода compare
def test_compare_a():
    list1 = [2, 4, 6]
    list2 = [1, 3, 5]
    result = Spiski.compare(list1, list2)
    assert result == "Первый список имеет большее среднее значение"


def test_compare_b():
    list1 = [2, 4, 6]
    list2 = [4, 6, 8]
    result = Spiski.compare(list1, list2)
    assert result == "Второй список имеет большее среднее значение"


def test_compare_ab():
    list1 = [7, 5, 6]
    list2 = [4, 6, 8]
    result = Spiski.compare(list1, list2)
    assert result == "Средние значения равны"
