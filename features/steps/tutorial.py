from behave import *


def _check_failure(state):
    if state:
        raise AssertionError()


@given('we have behave installed')
def step_given(context):
    _check_failure(context.failed)


@when('we implement a test')
def step_when(context):
    _check_failure(context.failed)


@then('behave will test it for us!')
def step_then(context):
    _check_failure(context.failed)
