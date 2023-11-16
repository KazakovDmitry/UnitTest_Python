import pytest
import os

# Тестирование создания и удаления файла
def test_create_and_remove_file():
    filename = "test_file.txt"
    with open(filename, "w") as file:
        file.write("Hello, World!")
    assert os.path.isfile(filename)
    os.remove(filename)
    assert not os.path.isfile(filename)