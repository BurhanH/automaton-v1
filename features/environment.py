from contextlib import contextmanager
from selenium import webdriver

WAIT_IMPL = 10
WINDOW_SIZE = 1280, 1024


@contextmanager
def _create_browser(context):
    yield
    context.webdriver.implicitly_wait(WAIT_IMPL)
    context.webdriver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])


def _create_firefox(context):
    with _create_browser(context):
        context.webdriver = webdriver.Firefox()


def _create_chrome(context):
    with _create_browser(context):
        context.webdriver = webdriver.Chrome()


def _close_webdriver(context):
    if "webdriver" in context:
        context.webdriver.close()


def before_tag(context, tag):
    if tag == "firefox":
        _create_firefox(context)
    if tag == "chrome":
        _create_chrome(context)


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    _close_webdriver(context)


def after_feature(context, feature):
    pass


def after_all(context):
    pass
