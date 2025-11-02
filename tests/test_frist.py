import time
import pytest
from selenium.webdriver.common.by import By
import logging

class TestFirst:
    def test_login(self,caplog):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='email']").send_keys("mkadam661@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Manish123")
        logging.info("Entered email successfully")
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="submit"]').click()
        time.sleep(2)
        contact_list=self.driver.find_element(By.XPATH,"//div[@class='main-content']//h1").text
        assert contact_list=="Contact List","not loaded contact list page"







