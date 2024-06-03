from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


add_to_cart_text = {"en": "Add to basket",
                    "fr": "Ajouter au panier",
                    "ru": "Добавить в корзину"}


def test_add_to_card_button(browser, user_language):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    cart_button_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                          "#add_to_basket_form button"))).text
    assert cart_button_text == add_to_cart_text.get(user_language), \
        f"Incorrect text on Cart button expected {user_language} but got {cart_button_text}"
