from driver import Driver
import random


class Resiliency(Driver):

    cpuUtilization = ''

    def go_to_resiliency(self):
        self.wait_for_visible_element_by_id("d3Graph")
        self.driver.find_element_by_id("dashboard-tab-nav").click()
        self.driver.find_element_by_id("resiliency-tab-nav").click()

    def wait_resiliency_to_load(self):
        self.wait_for_clickable_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
        print("======       User is on Resiliency page       =========")

    def scroll_down_to_utilization_and_errors(self):
        self.wait_for_clickable_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
        element = self.driver.find_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
        self.scroll_down_to_element(element)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def click_on_random_device_from_top_5_util_and_errors(self):
        cpuUtil = random.randint(1, 5)
        rand = str(cpuUtil)
        # wait_for_clickable_element_by_xpath(
        #     "//div[@id='utilization-component']/div/div[1]/table/tbody/tr["+str(cpuUtil)+"]/td[1]/a")
        self.cpuUtilization = self.driver.find_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[" + rand + "]/td[2]").get_attribute(
            'innerHTML')
        self.driver.find_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[" + rand + "]").click()
        # driver.execute_script("arguments[0].click();", element) --> we can execute script if element is nested and not clickable
