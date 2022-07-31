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
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_current_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(expected_current_url,browser.current_url)

    def test_b_failed_login_when_invalid_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("joko_ganteng") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(expected_message,actual_message)

    def test_c_failed_login_when_invalid_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("jokoganteng") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(expected_message,actual_message)

    def test_d_failed_login_when_blank_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Password is required"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(expected_message,actual_message)

    def test_e_failed_login_when_blank_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username is required"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(expected_message,actual_message)

    def test_f_failed_login_when_blank_username_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(0)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username is required"
        actual_message = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(expected_message,actual_message)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
