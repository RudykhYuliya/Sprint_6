import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить форму заказа')
    def create_order(self, order):
        self.set_value(OrderPageLocators.NAME_INPUT, order['name'])
        self.set_value(OrderPageLocators.SURNAME_INPUT, order['surname'])
        self.set_value(OrderPageLocators.ADDRESS_INPUT, order['address'])
        self.click(OrderPageLocators.METRO_INPUT)
        self.set_value(OrderPageLocators.METRO_INPUT, order['metro'])
        self.click(OrderPageLocators.metro_option(order['metro']))
        self.set_value(OrderPageLocators.PHONE_INPUT, order['phone'])
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.day_option(order['day']))
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.rent_option(order['rent']))
        self.click(OrderPageLocators.color_option(order['color']))
        self.set_value(OrderPageLocators.COMMENT_INPUT, order['comment'])
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def success_title(self):
        return self.get_text(OrderPageLocators.SUCCESS_TITLE)
