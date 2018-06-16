import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Driver:

    driver = webdriver.Chrome('utilities\chromedriver.exe')

    cpuUtilization = ''

    def scroll_down_to_element(self,  element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def wait_for_clickable_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            # You can write retry code here
            print("================== Wait for climbable element by xpath exception ==================")

    def wait_for_visible_element_by_id(self, id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, id)))
        except TimeoutException:
            # You can write retry code here
            print("================== Wait for visible element by ID exception ==================")

    @staticmethod
    def random_str(from_int, to_int):
        cpuUtil = random.randint(from_int, to_int)
        rand = str(cpuUtil)
        return rand

    def close_browser(self):
        time.sleep(3)
        self.driver.close()
        self.driver.quit()

    @staticmethod
    def wait(sec):
        time.sleep(sec)
