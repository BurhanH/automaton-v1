from contextlib import contextmanager
from selenium import webdriver

WAIT_IMPL = 10
WINDOW_SIZE = 1280, 1024


@contextmanager
def _get_driver(context) -> None:
    yield
    context.webdriver.implicitly_wait(WAIT_IMPL)
    context.webdriver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])


def _create_browser(context) -> None:
    command_line_browser = context.config.userdata.get('browser')
    if command_line_browser is not None:
        browser = command_line_browser.lower()
        if browser == 'chrome':
            _create_chrome(context)
        else:
            _create_firefox(context)
    else:
        # using Firefox browser by default
        _create_firefox(context)


def _create_firefox(context) -> None:
    with _get_driver(context):
        context.webdriver = webdriver.Firefox()
        # put some specific config here


def _create_chrome(context) -> None:
    with _get_driver(context):
        context.webdriver = webdriver.Chrome()
        # put some specific config here


def _close_webdriver(context) -> None:
    if "webdriver" in context:
        context.webdriver.close()


def before_tag(context, tag) -> None:
    pass


def before_all(context) -> None:
    pass


def before_feature(context, feature) -> None:
    pass


def before_scenario(context, scenario) -> None:
    _create_browser(context)


def before_step(context, step) -> None:
    pass


def after_step(context, step) -> None:
    pass


def after_scenario(context, scenario) -> None:
    _close_webdriver(context)


def after_feature(context, feature) -> None:
    pass


def after_all(context) -> None:
    pass
