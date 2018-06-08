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

