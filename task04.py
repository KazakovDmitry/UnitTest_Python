import pytest

# Тестирование добавления элемента в словарь
def test_dict_add():
    my_dict = {"key1": 1, "key2": 2}
    my_dict["key3"] = 3
    assert my_dict == {"key1": 1, "key2": 2, "key3": 3}

# Тестирование удаления элемента из словаря
def test_dict_remove():
    my_dict = {"key1": 1, "key2": 2}
    del my_dict["key1"]
    assert "key1" not in my_dict

# Тестирование поиска элемента в словаре
def test_dict_search():
    my_dict = {"key1": 1, "key2": 2}
    assert my_dict.get("key1") == 1
    assert my_dict.get("key3") is None

