from behave import *


@when('user goes to google')
def go_to(context):
    # Going to google.com
    context.webdriver.get('https://www.google.com')


@then('user able to search by term')
def enter_term_and_click_search_button(context):
    # Searching for the input field by name and entering data
    context.webdriver.find_element_by_name('q').send_keys('python')
    # Clicking Google Search button
    context.webdriver.find_element_by_css_selector("input[name='btnK']").click()
    # Verifying search results
    context.webdriver.find_element_by_class_name('bNg8Rb').is_displayed()
    # TODO Needs to add more verification/s