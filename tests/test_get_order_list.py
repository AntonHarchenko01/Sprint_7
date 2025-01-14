import allure
import requests


from urls import Urls


class TestGetOrderList:
    @allure.title('Тест проверки успешного получения списка заказов')
    @allure.description('Тест проверяет получения списка заказов, со станциями 4 и 7, получение кода 200 и id')
    def test_get_list_orders_without_parameters_received_list_orders(self):
        response = requests.get(Urls.GET_ORDERS, params={'nearestStation': '["4", "7"]'})
        assert response.status_code == 200 and 'id' in response.json()['orders'][0]
