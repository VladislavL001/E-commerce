from src.utils import path_data, open_data_file, create_obj_from_json
from unittest.mock import patch, Mock, mock_open
import pytest


@pytest.fixture
def mock_open_file() -> Mock:
    with patch("builtins.open", mock_open(
            read_data='[{"name": "Product1", "price": 100}, {"name": "Product2", "price": 200}]')) as mock_file:
        yield mock_file


@patch('os.path.dirname')
@patch('os.path.abspath')
def test_path_data(mock_abspath: Mock, mock_dirname: Mock) -> None:
    """Тест функции на правильный путь"""
    mock_dirname.return_value = '/home/user/project'
    mock_abspath.return_value = '/home/user/project/data/products.json'
    assert path_data() == '/home/user/project/data/products.json'


def test_open_data_file(mock_open_file: Mock) -> None:
    """Тест функции на открытие файла"""
    path = "mocked_path.json"
    expected_data = [{"name": "Product1", "price": 100}, {"name": "Product2", "price": 200}]
    result = open_data_file(path)
    mock_open_file.assert_called_once_with(path, "r", encoding="utf-8")
    assert result == expected_data
    mock_open_file().read.assert_called_once()


def test_create_obj_from_json_valid() -> None:
    """Тест функции на работу"""
    path = path_data()
    data = open_data_file(path)
    obj_category = create_obj_from_json(data)
    assert obj_category[0].name == "Смартфоны"

    assert obj_category[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert obj_category[0].products[1].name == "Iphone 15"
    assert obj_category[0].products[2].name == "Xiaomi Redmi Note 11"

    assert obj_category[1].name == "Телевизоры"
    assert obj_category[1].products[0].name == "55\" QLED 4K"


