from driver import Driver


class Login(Driver):

    def open_chrome(self):
        self.driver.maximize_window()
        Driver.driver.delete_all_cookies()

    def go_to_login(self, url):
        self.driver.get(url)

    def enter_username(self, nas):
        self.wait_for_visible_element_by_id('login-id')
        self.driver.find_element_by_id('login-id').send_keys(nas)

    def enter_password(self, password):
        self.wait_for_visible_element_by_id('login-password')
        self.driver.find_element_by_id('login-password').send_keys(password)

    def login(self):
        self.driver.find_element_by_id("login-submit").click()