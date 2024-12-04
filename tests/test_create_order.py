import allure
import pytest
from methods.order_methods import OrderMethods
from data import order_test_data

@allure.epic("Тестирование Заказов")
class TestCreateOrder:
    order_methods = OrderMethods()

    @pytest.mark.parametrize("order_data", order_test_data)
    @allure.title("Тест на создание заказа")
    @allure.description("Проверяет, что, когда создаёшь заказ: можно указать один из цветов — BLACK или GREY, можно указать оба цвета, можно совсем не указывать цвет, тело ответа содержит track.")
    def test_create_order(self, order_data):
        payload = {
            "firstName": order_data["first_name"],
            "lastName": order_data["last_name"],
            "address": order_data["address"],
            "metroStation": order_data["metro_station"],
            "phone": order_data["phone"],
            "rentTime": order_data["rent_time"],
            "deliveryDate": order_data["delivery_date"],
            "comment": order_data["comment"],
            "color": order_data["color"]
        }

        response = self.order_methods.create_order(payload)
        assert response.status_code == order_data[
            "expected_status"], f"Expected status {order_data['expected_status']}, but got {response.status_code}"
        assert "track" in response.json(), "Response does not contain 'track'"


