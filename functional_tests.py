from selenium import webdriver
import unittest
import time

# Create your tests here.


# class NewVisitorTest(unittest.TestCase):  

#     def setUp(self):  
#         self.browser = webdriver.Chrome()

#     def tearDown(self):  
#         self.browser.quit()

#     def test_can_start_a_list_and_retrieve_it_later(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Thomas Mills', self.browser.title)
#         time.sleep(2)

class CVPageTest(unittest.TestCase):  

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_button_redirection(self):
        self.browser.get('http://localhost:8000/cv')
        hrefs = self.browser.find_elements_by_class_name("top-menu")
        print(hrefs)
        for href in hrefs:
           try:
               self.assertIn(href, "/")
               print(href)
           except:
               print("not /")
           else:
               self.assertIn(href, "/cv/new/")
               print("ok")

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  