from behave import *


@given('browser')
def get_browser(context):
    pass


@when('set resolution')
def set_resolution(context):
    context.webdriver.set_window_size(800, 600)


@then('resolution is set')
def verify_resolution(context):
    resolution = context.webdriver.get_window_size()
    width = resolution.get('width')
    height = resolution.get('height')

    errors = []

    if width != 800:
        errors.append(u'With is {} expecting 800'.format(width))
    if height != 600:
        errors.append(u'Height is {} expecting 600'.format(height))

    error_msgs = '\n'.join(errors)

    # assert errors == [], error_msgs
    if errors:
        raise AssertionError(error_msgs)
