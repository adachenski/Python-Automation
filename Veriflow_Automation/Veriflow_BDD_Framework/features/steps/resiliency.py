from selenium_logic import resiliency_logic
from behave import step, given, when, then
resiliencyPage = resiliency_logic.Resiliency()


@step(u'Go to Resiliency page')
def step_impl(context):
    resiliencyPage.go_to_resiliency()


@step(u'Verify User is on Resiliency page')
def wait_page_to_load(context):
    resiliencyPage.wait_resiliency_to_load()