from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_start_list_and_retrive_later(self):
		self.browser.get('https://localhost:8000')
		self.assertIn('To-Do',self.browser,title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a To-Do item'
			)
		inputbox.send_keys('Buy Peacock Feathers')
		inputbox.send_keys(Keys.ENTER)
		time.sleep()

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1 : Buy Peacock Feathers' for row in rows)
		)

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')