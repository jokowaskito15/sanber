import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,"header_container > div.header_secondary_container > span").text

        self.assertEqual('Products', response_message)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()