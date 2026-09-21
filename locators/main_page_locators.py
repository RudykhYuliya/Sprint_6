from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class,"Header_Nav")]//button[text()="Заказать"]')
    FOOTER_ORDER_BUTTON = (
        By.XPATH,
        '//button[contains(@class,"Button_Middle") and text()="Заказать"]',
    )
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    QUESTIONS_SECTION = (By.CLASS_NAME, 'accordion')

    @staticmethod
    def question(index):
        return (By.ID, f'accordion__heading-{index}')

    @staticmethod
    def answer(index):
        return (By.ID, f'accordion__panel-{index}')
