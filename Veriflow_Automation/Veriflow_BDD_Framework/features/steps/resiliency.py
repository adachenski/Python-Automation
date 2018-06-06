from selenium_logic import resiliency_logic
from behave import step, given, when, then
resiliencyPage = resiliency_logic.Resiliency()


@step(u'Go to Resiliency page')
def step_impl(context):
    resiliencyPage.go_to_resiliency()


@step(u'Verify User is on Resiliency page')
def wait_page_to_load(context):
    resiliencyPage.wait_resiliency_to_load()


@given(u'Scroll down to Utilization and Errors section')
def scroll_down(context):
    resiliencyPage.scroll_down_to_utilization_and_errors()


@when(u'Click on random device from Top 5 CPU Utilization')
def click_on_random_device(context):
    resiliencyPage.click_on_random_device_from_top_5_util_and_errors()