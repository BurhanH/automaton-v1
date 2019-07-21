from behave import *


@given('browser')
def get_browser(context) -> None:
    pass


@when('browser set {resolution} resolution')
def set_resolution(context, resolution: str) -> None:
    res_list: list = resolution.rsplit(',')
    context.width: int = res_list[0]
    context.height: int = res_list[1]
    context.webdriver.set_window_size(context.width, context.height)


@then('resolution is set')
def verify_resolution(context) -> None:
    resolution = context.webdriver.get_window_size()
    width: int = resolution.get('width')
    height: int = resolution.get('height')

    errors: list = []

    if width != context.width:
        errors.append(f'Width is {width} expecting {context.width}')
    if height != context.height:
        errors.append(f'Height is {height} expecting {context.height}')

    error_msgs = '\n'.join(errors)

    if errors:
        raise AssertionError(error_msgs)
