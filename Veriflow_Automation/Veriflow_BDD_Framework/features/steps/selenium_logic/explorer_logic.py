from driver import Driver


class Explorer(Driver):

    def wait_for_graph_on_explorer(self):
        self.wait_for_visible_element_by_id("d3Graph")
        print("========    Device is shown on Explorer page  ========")

    def open_device_and_verify_cpu_utilization(self):
        print("cpu util: "+Driver.cpuUtilization)
        self.wait_for_clickable_element_by_xpath(
            "//li[@class='list-group-item side-bar-item searched']")
        self.driver.find_element_by_xpath(
            "//li[@class='list-group-item side-bar-item searched']").click()
        self.driver.find_element_by_xpath(
            "//li[@class='list-group-item side-bar-item searched active-item']//button").click()
        cpuIdle = self.driver.find_element_by_xpath(
            "//table[@id='device-property-table']//tr/th[text()='System CPU Idle']/../td").get_attribute('innerHTML')
        print('cpu idle: '+cpuIdle)