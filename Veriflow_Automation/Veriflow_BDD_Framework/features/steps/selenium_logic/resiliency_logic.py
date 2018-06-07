from driver import Driver


class Resiliency(Driver):

    random_str = Driver.random_str(1, 6)

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
        Driver.cpuUtilization = self.driver.find_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[" + self.random_str + "]/td[2]").get_attribute(
            'innerHTML')
        print("cpu utilllll"+self.cpuUtilization)
        # wait_for_clickable_element_by_xpath(
        #     "//div[@id='utilization-component']/div/div[1]/table/tbody/tr["+str(cpuUtil)+"]/td[1]/a")
        self.driver.find_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[" + self.random_str + "]").click()
        # driver.execute_script("arguments[0].click();", element) --> we can execute script if element is nested and not clickable



