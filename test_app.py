import unittest
import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_index_should_return_hello_world_html(self):
        response = self.app.get('/')
        self.assertIn(b'iPropSQ', response.data)

    def test_index_should_use_correct_template(self):
        response = self.app.get('/')
        self.assertIn(b'<title>iPropSQ</title>', response.data)


if __name__ == '__main__':
    unittest.main()
