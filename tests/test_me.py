from unittest import TestCase
from unittest.mock import patch
from src.pythontemplate.example import add_one, add_with_args


class TestExtraction(TestCase):
    def setUp(self) -> None:
        pass

    def test_add(self):
        x = add_one(3)
        self.assertEqual(x, 4)

    @patch('src.pythontemplate.example.add_one')
    def test_add_with_mock(self, mock_add_one):
        mock_add_one.return_value = 2
        actual = add_with_args(1)
        self.assertEqual(2, actual)
