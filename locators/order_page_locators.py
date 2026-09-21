from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.CLASS_NAME, 'select-search__input')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (
        By.XPATH,
        '//button[contains(@class,"Button_Middle") and text()="Заказать"]',
    )
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_TITLE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    @staticmethod
    def metro_option(station):
        return (By.XPATH, f'//button[.//div[text()="{station}"]]')

    @staticmethod
    def day_option(day):
        return (
            By.XPATH,
            f'//div[contains(@class,"react-datepicker__day") and not(contains(@class,"outside-month")) and text()="{day}"]',
        )

    @staticmethod
    def rent_option(period):
        return (By.XPATH, f'//div[@class="Dropdown-option" and text()="{period}"]')

    @staticmethod
    def color_option(color):
        return (By.ID, color)
