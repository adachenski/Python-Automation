from selenium_logic import explorer_logic
from behave import step, given, when, then
explorerPage = explorer_logic.Explorer()


@when(u'Verify that device is shown on Explorer page')
def verify_device_is_shown_on_explorer(context):
    explorerPage.wait_for_graph_on_explorer()


@when(u'Open Device Details and Verify CPU Utilization value')
def verify_cpu_utilization(context):
    explorerPage.open_device_and_verify_cpu_utilization()
