from selenium.webdriver.common.by import By
from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.customer_login import CustomerLogin


# TODO НЕ красивый станндартный тест
def test_incorrect_login(driver):
    login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.fill_login_form('dfsdfs@aad.com', 'sdfsdfsd')
    # WebDriverWait(driver, 5).until(ec.staleness_of(button))
    login_page.check_error_alert(
            'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
        )
