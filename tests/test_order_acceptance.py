import time

import allure

from data import ORDER_DATA_1
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@allure.epic("Тестирование Принятия Заказов")
class TestOrderAcceptance:
    order_methods = OrderMethods()
    courier_methods = CourierMethods()

    @allure.title("Тест на успешное принятие заказа")
    @allure.description("Создает курьера и заказ, затем проверяет успешное принятие заказа курьером.")
    def test_accept_order_success(self):

        courier_payload = self.courier_methods.generate_courier_data()
        self.courier_methods.create_courier(courier_payload)
        courier_id = self.courier_methods.get_courier_id(courier_payload['login'], courier_payload['password'])

        response = self.order_methods.create_order(ORDER_DATA_1)
        assert response.status_code == 201

        order_data = response.json()
        print(f"Order Response: {order_data}")
        assert "track" in order_data
        order_id = str(order_data["track"])
        time.sleep(25)
        order_status_response = self.order_methods.get_order_by_id(order_id)
        assert order_status_response.status_code == 200

        acceptance = self.order_methods.accept_order(order_id, courier_id)
        print(acceptance.json())
        assert acceptance.status_code == 200
        assert acceptance.json() == {"ok": True}


    @allure.title("Тест на принятие заказа без указания ID курьера")
    @allure.description("Проверяет, что попытка принятия заказа без указания ID курьера возвращает статус 400.")
    def test_accept_order_missing_courier_id(self):
        response = self.order_methods.create_order(ORDER_DATA_1)
        order_data = response.json()
        order_id = str(order_data["track"])
        acceptance = self.order_methods.accept_order(order_id, courier_id= None)
        assert acceptance.status_code == 400
        assert acceptance.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Тест на принятие заказа с невалидным ID курьера")
    @allure.description("Проверяет, что принятие заказа с невалидным ID курьера возвращает статус 404.")
    def test_accept_order_invalid_courier_id(self):
        response = self.order_methods.create_order(ORDER_DATA_1)
        order_data = response.json()
        order_id = str(order_data["track"])
        acceptance = self.order_methods.accept_order(order_id, courier_id=-1)
        assert acceptance.status_code == 404
        assert acceptance.json()["message"] == "Курьера с таким id не существует"

    @allure.title("Тест на принятие заказа без указания ID заказа")
    @allure.description("Проверяет, что принятие заказа без указания ID заказа возвращает статус 404.")
    def test_accept_order_missing_order_id(self):
        courier_payload = self.courier_methods.generate_courier_data()
        self.courier_methods.create_courier(courier_payload)
        courier_id = self.courier_methods.get_courier_id(courier_payload['login'], courier_payload['password'])

        acceptance = self.order_methods.accept_order(order_id = "", courier_id=courier_id)
        assert acceptance.status_code == 404
        assert acceptance.json()["message"] == "Not Found."

    @allure.title("Тест на принятие заказа с невалидным ID заказа")
    @allure.description("Проверяет, что принятие заказа с невалидным ID заказа возвращает статус 404.")
    def test_accept_order_invalid_order_id(self):
        courier_payload = self.courier_methods.generate_courier_data()
        self.courier_methods.create_courier(courier_payload)
        courier_id = self.courier_methods.get_courier_id(courier_payload['login'], courier_payload['password'])
        acceptance = self.order_methods.accept_order(order_id=-1, courier_id=courier_id)
        assert acceptance.status_code == 404
        assert acceptance.json()["message"] == "Заказа с таким id не существует"
