import unittest
import re
from app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
      tester = app.test_client(self)
      response = tester.get('/', content_type='html/text')
      self.assertEqual(response.status_code, 200)
      self.assertRegexpMatches(response.data, b'Hello World! I have been seen') #Hello World! I have been seen 5 times.
    def test_other(self):
      tester = app.test_client(self)
      response = tester.get('a', content_type='html/text')
      self.assertEqual(response.status_code, 404)
      self.assertFalse(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()