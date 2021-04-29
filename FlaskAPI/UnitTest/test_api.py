import FlaskAPI.Home as app
# import FlaskAPI.Search as app
# import FlaskAPI.Upload as app

# https://docs.python.org/3/library/unittest.html

import unittest
import json


class FlaskTestCase(unittest.TestCase):

    def test_read(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_read_contentType(self):
        tester = app.test_client(self)
        response = tester.get("/")
        print(response.content_type)
        # self.assertEqual(response.content_type,"text/html; charset=utf-8")

    def test_read_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        print(response.data)
        # self.assertEqual(response.data.decode(),"Done")
