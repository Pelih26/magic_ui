from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_field = self.driver.find_element(By.ID, 'email')
        password_field = self.driver.find_element(By.ID, 'pass')
        button = self.driver.find_element(By.ID, 'send2')
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    def check_error_alert(self, text):
        # WebDriverWait(driver, 5).until(ec.staleness_of(button))
        error_alert = (self.driver.find_element
                       (By.CSS_SELECTOR,
                        '[data-bind = "html: $parent.prepareMessageForHtml(message.text)"]'))
        assert error_alert.text == text
