from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_start_list_and_retrive_later(self):
		self.browser.get('https://localhost:8000')
		self.assertIn('To-Do',self.browser,title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')