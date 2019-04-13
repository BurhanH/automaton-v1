import time

from behave import *

# It's a bad practice
TIMEOUT = 1  # in sec


@when('user goes to google')
def go_to(context):
    # Going to google.com
    context.webdriver.get('https://www.google.com')


@then('user able to search by {target_text} term')
def enter_term_and_click_search_button(context, target_text):
    # Searching for the input field by name and entering data
    search_textfield = context.webdriver.find_element_by_name('q')
    search_textfield.is_displayed()
    search_textfield.is_enabled()
    search_textfield.send_keys(target_text)
    time.sleep(TIMEOUT)
    # Searching and waiting the search drop-down menu
    menu = context.webdriver.find_element_by_css_selector('.FPdoLc.VlcLAe')
    menu.is_displayed()
    menu.is_enabled()
    time.sleep(TIMEOUT)
    # Clicking Google Search button
    search_btn = context.webdriver.find_element_by_css_selector("input[name='btnK']")
    search_btn.is_displayed()
    search_btn.is_enabled()
    search_btn.click()
    time.sleep(TIMEOUT)
    # Verifying search results
    context.webdriver.find_element_by_css_selector('.bNg8Rb').is_displayed()
    # TODO Needs to add more verification/s
