
BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_LOGIN_URL = f'{BASE_URL}/api/v1/courier/login'
COURIER_REGISTRATION_URL = f'{BASE_URL}/api/v1/courier'
CREATE_ORDER_URL= f'{BASE_URL}/api/v1/orders'
CANCEL_ORDER_URL= f'{BASE_URL}/api/v1/orders/cancel'
GET_ORDERS_URL = f'{BASE_URL}/api/v1/orders'
ACCEPT_ORDER_URL = f'{BASE_URL}/api/v1/orders/accept/'


ORDER_DATA_1= {
        "first_name": "Naruto",
        "last_name": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metro_station": 4,
        "phone": "+7 800 355 35 35",
        "rent_time": 5,
        "delivery_date": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"],
        "expected_status": 201
    }