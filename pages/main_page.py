import allure

from data import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.open_url(BASE_URL)
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажать Заказать в шапке')
    def open_order_from_header(self):
        self.click(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Нажать Заказать внизу страницы')
    def open_order_from_footer(self):
        self.click(MainPageLocators.FOOTER_ORDER_BUTTON)

    @allure.step('Открыть вопрос о важном')
    def answer_text(self, index):
        self.click(MainPageLocators.question(index))
        return self.get_text(MainPageLocators.answer(index))

    @allure.step('Нажать логотип Самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать логотип Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_last_window()

    def is_main_page_opened(self):
        self.wait_visible(MainPageLocators.QUESTIONS_SECTION)
        return self.get_current_url().rstrip('/') == BASE_URL.rstrip('/')

    def is_dzen_opened(self):
        self.wait_for_url(
            lambda url: 'dzen.ru' in url or url.rstrip('/') == 'https://ya.ru'
        )
        url = self.get_current_url()
        return 'dzen.ru' in url or url.rstrip('/') == 'https://ya.ru'
