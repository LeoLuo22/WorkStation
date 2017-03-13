# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerCase
#from django.test import LiveServerTestCase

class NewVisitorTest(StaticLiveServerCase):

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        self.brower.refresh()
        self.brower.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get('http://127.0.0.1:8000')
        self.assertIn('To-Do', self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.brower.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        inputbox = self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #self.fail('Finish the test')
        self.brower.quit()
        self.brower = webdriver.Firefox()

        self.brower.get('localhost:8000')
        page_text = self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        francis_list_url = self.brower.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #This page contains the list without Edith
        page_text = self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #They're both happy and go to bed

    def test_layout_and_styling(self):
        #Edith visit the home page
        self.brower.get('http://127.0.0.1:8000')
        self.brower.set_window_size(1024, 768)

        #She saw the input box is in the middle
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=6)
        #She created a new list and still the input box is in the middle
        inputbox.send_keys('testing\n')
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)
