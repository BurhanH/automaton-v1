from behave import *


@given('browser')
def get_browser(context):
    pass


@when('browser set {resolution} resolution')
def set_resolution(context, resolution):
    res_list = resolution.rsplit(',')
    context.width = int(res_list[0])
    context.height = int(res_list[1])
    context.webdriver.set_window_size(context.width, context.height)


@then('resolution is set')
def verify_resolution(context):
    resolution = context.webdriver.get_window_size()
    width = resolution.get('width')
    height = resolution.get('height')

    errors = []

    if width != context.width:
        errors.append(u'Width is {} expecting {}'.format(width, context.width))
    if height != context.height:
        errors.append(u'Height is {} expecting {}'.format(height, context.height))

    error_msgs = '\n'.join(errors)

    if errors:
        raise AssertionError(error_msgs)
