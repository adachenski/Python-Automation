from driver import Driver


class Resiliency(Driver):

    def go_to_resiliency(self):
        self.wait_for_visible_element_by_id("d3Graph")
        self.driver.find_element_by_id("dashboard-tab-nav").click()
        self.driver.find_element_by_id("resiliency-tab-nav").click()

    def wait_resiliency_to_load(self):
        self.wait_for_clickable_element_by_xpath(
            "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
        print("======       User is on Resiliency page       =========")