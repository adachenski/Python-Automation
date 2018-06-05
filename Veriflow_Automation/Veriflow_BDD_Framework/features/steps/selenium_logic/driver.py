from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Driver:

    driver = webdriver.Chrome('utilities\chromedriver.exe')

    def wait_for_clickable_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            # You can write retry code here
            print("================== Nasko TimeoutException ==================")

    def wait_for_visible_element_by_id(self, id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, id)))
        except TimeoutException:
            # You can write retry code here
            print("================== Nasko TimeoutException ==================")