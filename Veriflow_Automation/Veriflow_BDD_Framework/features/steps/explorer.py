from selenium_logic import explorer_logic
from behave import step, given, when, then
explorerPage = explorer_logic.Explorer()


@when(u'Verify that device is shown on Explorer page')
def verify_device_is_shown_on_explorer(context):
    explorerPage.wait_for_graph_on_explorer()


@when(u'Open Device Details and Verify CPU Utilization value')
def verify_cpu_utilization(context):
    explorerPage.open_device_and_verify_cpu_utilization()


@step(u'Load snapshot Flow Model from the navigation menu')
def load_current_flow_model(context):
    explorerPage.load_snapshot_flow_model()


@step(u'Verify that Graph is shown on Explorer page')
def wait_for_graph(context):
    explorerPage.wait_for_graph_on_explorer()


@when(u'Click into the search box and enter "{query}"')
def enter_query_into_search_box(context, query):
    explorerPage.wait(1)
    explorerPage.enter_query_into_search_box(query)


@when(u'Execute the query')
def execute_query(context):
    explorerPage.execute_query()


@then(u'Verify the query')
def verify_query(context):
    explorerPage.wait(1)
