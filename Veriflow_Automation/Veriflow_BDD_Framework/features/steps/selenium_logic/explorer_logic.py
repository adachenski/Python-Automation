from driver import Driver


class Explorer(Driver):

    count = 1

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

    def load_snapshot_flow_model(self):
        self.driver.find_element_by_id("snapshot-loading-progress").click()
        self.driver.find_element_by_xpath("//button[@data-load='flow']").click()

    def enter_query_into_search_box(self, query):
        self.wait(3)
        if self.count == 1:
            self.driver.find_element_by_xpath("//form[@id='search-container']/div/textarea").send_keys(query)
            self.count += 1
        else:
            self.driver.find_element_by_xpath("//form[@id='search-container']/div/div/textarea").clear()
            self.driver.find_element_by_xpath("//form[@id='search-container']/div/div/textarea").send_keys(query)

    def execute_query(self):
        self.driver.find_element_by_id("btn-network-search").click()
