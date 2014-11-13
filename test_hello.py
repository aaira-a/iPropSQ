import unittest
import hello


class HelloTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hello.app.test_client()

    def test_index_should_return_hello_world_html(self):
        response = self.app.get('/')
        assert b'Hello World!' in response.data

    def test_index_should_use_correct_template(self):
        response = self.app.get('/')
        assert b'<title>Hello</title>' in response.data

    @unittest.skip
    def test_request001_should_return_fetched_data_from_api(self):
        response = self.app.get('/request001')
        assert b"{\"code\":200}" in response.data


if __name__ == '__main__':
    unittest.main()
