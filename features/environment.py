from selenium import webdriver


def _create_webdriver(context):
    context.webdriver = webdriver.Firefox()


def _close_webdriver(context):
    if 'webdriver' in context:
        context.webdriver.close()


def before_all(context):
    pass


def before_feature(context, feature):
    _create_webdriver(context)


def before_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    _close_webdriver(context)


def after_all(context):
    pass
