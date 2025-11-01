import time

import pytest
from selenium.webdriver.common.by import By


class TestLogout:
    @pytest.mark.order(1)
    def test_logout(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys("mkadam661@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Manish123")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(2)
        contact_list = self.driver.find_element(By.XPATH, "//div[@class='main-content']//h1").text
        assert contact_list == "Contact List", "not loaded contact list page"
        time.sleep(2)
        self.driver.find_element(By.ID,"logout").click()
        time.sleep(1)
        login_test=self.driver.find_element(By.XPATH,"//div[@class='main-content']/p[1]").text
        assert login_test=="Log In:","Logout not done successfully"
