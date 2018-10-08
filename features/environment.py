from selenium import webdriver
WAIT_IMPL = 10


def _create_firefox(context):
        context.webdriver = webdriver.Firefox()
        context.webdriver.implicitly_wait(WAIT_IMPL)


def _close_webdriver(context):
    if 'webdriver' in context:
        context.webdriver.close()


def before_tag(context, tag):
    if tag == "firefox":
        _create_firefox(context)


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
