from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAMBURGER_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop a.nav-a')
BESTSELLERS_BUTTON = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
BESTSELLERS_LINK = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq  div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")
COLOR_OPTIONS = (By.CSS_SELECTOR, ".imgSwatch")
CURRENT_COLOR = (By.CSS_SELECTOR, ".selection")
MUG_IMG = (By.CSS_SELECTOR, ".s-image")
MUG_PRODUCT_NAME = (By.CSS_SELECTOR, "img[data-image-latency='s-product-image']")
BEST_SELLER_ROOT=(By.CSS_SELECTOR, "#zg_header a")
LOCATORR=(By.CSS_SELECTOR, "#zg_banner_text")


@given('Open amazon Product page')
def jean_colors(context):
    context.driver.get('https://www.amazon.com/Dickies-Mens-Original-Work-Black/dp/B000N8PZ8G/')
    context.driver.implicitly_wait(5)


@given('Open Amazon bestseller page')
def open_bestseller(context):
    #context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.app.main_page.best_seller()
@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()
    context.driver.implicitly_wait(5)

@given('open new arrivals')
def open_new_arrivals(context):
    context.app.main_page.new_arrivals()
    context.driver.implicitly_wait(5)


@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search_button(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Hover over on language option')
def hover_language_options(context):
    context.app.header.hover_language_options()

@when('Hover over on new arrivals option')
def hover_new_arrivals(context):
    context.app.header.new_arrivals_shown()



@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)




@then('Verify user can click on all best seller links')
def best_seller_links(context):
    first_link = context.driver.find_elements(*BEST_SELLER_ROOT)
    print(first_link)

    for a in range(len(first_link)):
        to_click = context.driver.find_elements(*BEST_SELLER_ROOT)[a]
        link_text = to_click.text
        print(link_text)
        to_click.click()
        header_text = context.driver.find_element(*LOCATORR).text
        print(header_text)
        assert link_text in header_text,f'expected{link_text} in {header_text}'


@then('Verify user can click on all the colors')
def jean_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()
    all_jean_color = context.driver.find_elements(*COLOR_OPTIONS)
    print('All jean colors:', all_jean_color)
    for jeans in all_jean_color:
        jeans.click()
        current_jean_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color:', current_jean_color)


@then('Verify that all the mug images visible')
def visibility_of_mugs(context):
    context.driver.find_elements(*MUG_IMG)
    element_img = context.driver.find_elements(*MUG_IMG)
    expected_result = len(element_img)
    assert len(element_img) == expected_result, f'expected{MUG_IMG}but got {len(element_img)}'
    print('Images:', len(element_img))
    print('All images present')


@then('Verify product names are present')
def product_names(context):
    context.driver.find_elements(*MUG_PRODUCT_NAME)
    all_mug_names = context.driver.find_elements(*MUG_PRODUCT_NAME)
    print('Product names:', len(all_mug_names))
    print('All stable product has a name')

    #for product in all_products:
    #print(product)
    #assert product.find_element(*mug_image).is_displayed(), 'product image is missing'
    #print(product.find_element(*mug_product_name).text)
    #assert product.find_element(*mug_product_name).text, 'product name is missng'


@then('Click on bestsellers button')
def bestsellers_button(context):
    context.driver.find_element(*BESTSELLERS_BUTTON).click()


@then('Verify hamburger menu icon present')
def hamburger_menu(context):
    #print('\n find element:')
    element = context.driver.find_element(*HAMBURGER_MENU)
    print(element)


@then('Verify that footer has {expected_amount_of_links} links')
def verify_footer_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print('\n Link count :', len(footer_links))
    assert len(footer_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(footer_links)}'


@then('Verify that header has {expected_amount_of_links} links')
def verify_header_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    print('\n Link count :', len(header_links))
    assert len(header_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(header_links)}'


@then('Verify that bestsellers option has {expected_amount_of_links} links')
def verify_header_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    Bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINK)
    print('\n Link count :', len(Bestsellers_links))
    assert len(Bestsellers_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(Bestsellers_links)}'


@then('Verify user can see Language section')
def verify_language_option_shown(context):
    context.app.header.verify_language_shown()


@then('Verify user can see new deals')
def verify_new_arrivals_shown(context):
    context.app.header.new_arrivals_shown()