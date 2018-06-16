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
        if self.count == 1:
            self.driver.find_element_by_xpath("//div[@id='search-field-pane']/div/div/div/textarea").send_keys(query)
            self.count += 1
        else:
            self.driver.find_element_by_xpath("//div[@id='search-field-pane']/div/div/div/div/textarea").clear()
            self.driver.find_element_by_xpath("//div[@id='search-field-pane']/div/div/div/div/textarea").send_keys(query)

    def execute_query(self):
        self.driver.find_element_by_id("btn-network-search").click()

    def click_on_advanced(self):
        self.wait_for_visible_element_by_id("left-bar")
        self.wait(1)
        self.driver.find_element_by_xpath("//li[@id='search-field-tab']").click()

    def verify_devices_paths(self, devices, paths):
        self.wait(2)
        paths_returned = self.driver.find_element_by_xpath("//li[@id='flow-tab-nav']/a").text
        devices_returned = self.driver.find_element_by_xpath("//li[@id='device-tab-nav']/a").text

        if paths_returned == paths and devices_returned == devices:
            print("Paths and Devices OK")
        else:
            print("Selenium VS Veriflow app result: " + devices_returned + " NOT " + devices)
            print("Selenium VS Veriflow app result: " + paths_returned + " NOT " + paths)
            raise Exception("Devices or Flow Paths values mismatch")
