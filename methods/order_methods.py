import allure
import requests

from data import CREATE_ORDER_URL, GET_ORDERS_URL, ACCEPT_ORDER_URL


class OrderMethods:

    @allure.step("Создаем заказ с данными")
    def create_order(self, payload):
        return requests.post(CREATE_ORDER_URL, json=payload)

    @allure.step("Получаем список всех заказов")
    def get_orders(self):
        response = requests.get(GET_ORDERS_URL)
        return response

    @allure.step("Принимаем заказ с ID заказа и курьера")
    def accept_order(self, order_id, courier_id):
        if courier_id is not None:
            url = f'{ACCEPT_ORDER_URL}{order_id}?courierId={courier_id}'
        else:
            url = f'{ACCEPT_ORDER_URL}{order_id}?courierId='

        response = requests.put(url)
        return response

    @allure.step("Получаем заказ по ID")
    def get_order_by_id(self, order_id):
        return requests.get(f'{GET_ORDERS_URL}/track?t={order_id}')
