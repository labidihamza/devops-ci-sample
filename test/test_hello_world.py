import unittest
from io import StringIO
from unittest.mock import patch
import hello_world 

class TestHelloWorld(unittest.TestCase):

    def test_get_name(self):
        with patch('builtins.input', return_value='John'):
            self.assertEqual(hello_world.get_name(), 'John')

    def test_display_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            hello_world.display_name('Mary')
            self.assertEqual(fake_output.getvalue().strip(), 'Hello Mary!')

if __name__ == '__main__':
    unittest.main()

