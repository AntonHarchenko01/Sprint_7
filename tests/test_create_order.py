import allure
import pytest
import requests
from data import data_order_color_black, data_order_color_grey, data_order_color_black_and_grey, data_order_not_color
from urls import Urls


class TestCreateOrder:
    @allure.title('Тест проверки успешного создания заказа')
    @allure.description('Тест проверяет успешное создание заказа с разными значениями поля color, получение кода 201 и сообщения {"ok": True}')
    @pytest.mark.parametrize('data_order', [data_order_color_black, data_order_color_grey, data_order_color_black_and_grey, data_order_not_color])
    def test_create_order_different_color_field_value_order_create(self, data_order):
        payload = data_order
        response = requests.post(Urls.CREATE_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.json()
