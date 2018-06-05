from selenium_logic import login_logic
from behave import step, given, when, then
loginPage = login_logic.Login()


@given(u'Open Chrome Browser')
def open_browser(context):
    loginPage.open_chrome()


@when(u'Navigate to Veriflow Login page at "{url}"')
def navigate_to_url(context, url):
    loginPage.go_to_login(url)


@when(u'Enter username "{nas}"')
def username(context, nas):
    loginPage.enter_username(nas)


@when(u'Enter password "{password}"')
def password(context, password):
    loginPage.enter_password(password)


@then(u'Click on Login Tab')
def login(context):
    loginPage.login()


#
#
# @given(u'Scroll down to Utilization and Errors section')
# def step_impl(context):
#     wait_for_clickable_element_by_xpath(
#         "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
#     element = driver.find_element_by_xpath(
#         "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[1]/td[1]/a")
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#     #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#
#
# @when(u'Click on random device from "{section}"')
# def step_impl(context, section):
#     allSections = ['Top 5 CPU Utilization', 'Top 5 Memory Utilization',
#                    'Top 5 Utilized Interfaces', 'Top 5 CRC Error Count',
#                    'Top 5 (Shortest) Uptime', 'Top 5 (Longest) Uptime']
#     randNumber = random.randint(1, 5)
#     rand = str(randNumber)
#     print('=============================  '+section)
#     currentSection = allSections.index(section)+1
#     print(currentSection)
#     print("=================================")
#     y = str(currentSection)
#     # wait_for_clickable_element_by_xpath(
#     #     "//div[@id='utilization-component']/div/div["+ y +"]/table/tbody/tr[" + x + "]/td[1]/a")
#     context.cpuUtilization = driver.find_element_by_xpath(
#         "//div[@id='utilization-component']/div/div[1]/table/tbody/tr[" + rand + "]/td[2]").get_attribute('innerHTML')
#     driver.find_element_by_xpath(
#         "//div[@id='utilization-component']/div/div["+ y +"]/table/tbody/tr[" + rand + "]").click()
#     time.sleep(2)
#
#
# @when(u'Click on random device from Top 5 CPU Utilization')
# def step_impl(context):
#     cpuUtil = random.randint(1,5)
#     rand = str(cpuUtil)
#     # wait_for_clickable_element_by_xpath(
#     #     "//div[@id='utilization-component']/div/div[1]/table/tbody/tr["+str(cpuUtil)+"]/td[1]/a")
#     context.cpuUtilization = driver.find_element_by_xpath(
#         "//div[@id='utilization-component']/div/div[1]/table/tbody/tr["+ rand +"]/td[2]").get_attribute('innerHTML')
#     driver.find_element_by_xpath(
#         "//div[@id='utilization-component']/div/div[1]/table/tbody/tr["+ rand +"]").click()
#     #driver.execute_script("arguments[0].click();", element) --> we can execute script if element is nested and not clickable
#
#
# @when(u'Open Device Details and Verify CPU Utilization value')
# def verify_cpu_utilization(context):
#     print(context.cpuUtilization)
#     wait_for_clickable_element_by_xpath(
#         "//li[@class='list-group-item side-bar-item searched']")
#     driver.find_element_by_xpath(
#         "//li[@class='list-group-item side-bar-item searched']").click()
#     driver.find_element_by_xpath(
#         "//li[@class='list-group-item side-bar-item searched active-item']//button").click()
#     cpuIdle = driver.find_element_by_xpath(
#         "//table[@id='device-property-table']//tr/th[text()='System CPU Idle']/../td").get_attribute('innerHTML')
#     print(cpuIdle)
#
#
# @when(u'Verify that device is shown on Explorer page')
# def step_impl(context):
#     wait_for_visible_element_by_id("d3Graph")
#     print("========    Device is shown on Explorer page  ========")
#
#

#
#
# @then(u'I close the browser')
# def step_impl(contex):
#     close_browser(driver)
#
#
#
# def close_browser(web_browser):
#     time.sleep(3)
#     web_browser.close()
#     web_browser.quit()
#
