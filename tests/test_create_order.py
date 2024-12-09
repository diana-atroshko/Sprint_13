import allure
import pytest
from methods.order_methods import OrderMethods

@allure.epic("Тестирование Заказов")
class TestCreateOrder:
    order_methods = OrderMethods()

    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    @allure.title("Тест на создание заказа")
    @allure.description("Проверяет, что, когда создаёшь заказ: можно указать один из цветов — BLACK или GREY, можно указать оба цвета, можно совсем не указывать цвет, тело ответа содержит track.")
    def test_create_order(self, color):
        order_data = {
            "first_name": "Naruto",
            "last_name": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metro_station": 4,
            "phone": "+7 800 355 35 35",
            "rent_time": 5,
            "delivery_date": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        response = self.order_methods.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json(), "Response does not contain 'track'"


