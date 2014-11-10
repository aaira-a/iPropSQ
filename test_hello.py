import unittest
import hello


class HelloTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hello.app.test_client()

    def test_index_should_return_hello_world_html(self):
        response = self.app.get('/')
        assert b'Hello World!' in response.data

if __name__ == '__main__':
    unittest.main()
