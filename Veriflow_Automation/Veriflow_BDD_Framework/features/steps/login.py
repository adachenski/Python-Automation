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


@then(u'I close the browser')
def step_impl(contex):
    loginPage.close_browser()



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



