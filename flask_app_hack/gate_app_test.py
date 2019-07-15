import unittest

from game_app import app


class TestHealthPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        # app.config['Testing'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['Debug'] = False
        # self.app = app.test_client()
        # self.assertEqual(app.debug, False)

    def test_main_page(self):
        responce = self.app.get('/_health')
        print(responce)
        self.assertEqual(responce.status_code, 200)
