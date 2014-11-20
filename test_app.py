import unittest
import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_index_should_return_app_name_html(self):
        response = self.app.get('/')
        self.assertIn(b'iPropSQ', response.data)

    def test_index_should_use_correct_template(self):
        response = self.app.get('/')
        self.assertIn(b'<title>iPropSQ</title>', response.data)


class ResultViewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_result_view_should_use_correct_template(self):
        response = self.app.get('/results')
        self.assertIn(b'<title>Nearby', response.data)


if __name__ == '__main__':
    unittest.main()
