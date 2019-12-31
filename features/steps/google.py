import time

from behave import when, then
from selenium.webdriver.common.keys import Keys

# It's a bad practice
TIMEOUT = 2  # in sec


@when('user goes to google')
def go_to(context) -> None:
    # Going to google.com
    context.webdriver.get('https://www.google.com')


@then('user able to search by {target_text} term')
def enter_term_and_click_search_button(context, target_text: str) -> None:
    # Searching for the input field by name and entering data
    search_textfield = context.webdriver.find_element_by_name('q')
    search_textfield.is_displayed()
    search_textfield.is_enabled()
    search_textfield.send_keys(target_text + Keys.ENTER)
    time.sleep(TIMEOUT)
    # Verifying search results
    context.webdriver.find_element_by_css_selector('.bNg8Rb').is_displayed()
    # TODO Needs to add more verification/s
