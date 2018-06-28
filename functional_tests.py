from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser =webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        # page title and header must mention 'To-Do'
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')

        # 1 invited to enter a to-do item straigh away
        # 2 type into a textbox: buy item1,
        # 3 hit enter and see that page refreshes and item is added to to-do list
        # repeat steps 1-3, but add item2 instead
        # get a unique url
        # revisit url to check that list still exists

if __name__=='__main__':
    unittest.main(warnings='ignore')
