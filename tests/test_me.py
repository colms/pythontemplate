from unittest import TestCase
from unittest.mock import patch
from tests.utils import read_json_resource_file
from src.pythontemplate.example import add_one, add_with_args


class TestExample(TestCase):
    def setUp(self) -> None:
        pass

    def test_add(self):
        x = add_one(3)
        self.assertEqual(4, x)

    @patch('src.pythontemplate.example.add_one')
    def test_add_with_mock(self, mock_add_one):
        mock_add_one.return_value = 2
        actual = add_with_args(1)
        self.assertEqual(2, actual)

    def test_from_file(self):
        json_dict = read_json_resource_file('file.json')
        self.assertEqual(5, json_dict['my_number'])
