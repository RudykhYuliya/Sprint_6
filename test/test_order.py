import allure
import pytest

from data import ORDER_1, ORDER_2
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrder:
    @allure.title('Позитивный сценарий заказа')
    @pytest.mark.parametrize(
        'open_order, order',
        [
            (MainPage.open_order_from_header, ORDER_1),
            (MainPage.open_order_from_footer, ORDER_2),
        ],
        ids=['header', 'footer'],
    )
    def test_successful_order(self, main_page, open_order, order):
        open_order(main_page)
        order_page = OrderPage(main_page.driver)
        order_page.create_order(order)
        assert 'Заказ оформлен' in order_page.success_title()

    @allure.title('Логотип Самоката открывает главную')
    def test_scooter_logo_opens_main_page(self, main_page):
        main_page.open_order_from_header()
        main_page.click_scooter_logo()
        assert main_page.is_main_page_opened() == True

    @allure.title('Логотип Яндекса открывает Дзен')
    def test_yandex_logo_opens_dzen(self, main_page):
        main_page.click_yandex_logo()
        assert main_page.is_dzen_opened() == True
