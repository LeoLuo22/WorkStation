# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get('http://localhost:8000')
        self.assertIn('To-DO', self.brower.title)
        self.fail('Finish the test')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
