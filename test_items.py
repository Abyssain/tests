import time

def test_existence_of_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket').is_displayed(), \
    'Кнопка добавления товара в корзину отсутствует'
