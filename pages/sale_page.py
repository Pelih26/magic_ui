from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_title(self, text):
        header_title = self.driver.find_element(By.TAG_NAME, 'h1')
        assert header_title.text == text
