

# this helper class is used in TestData class below to select delivery payment method
class DeliveryPaymentMethodOptions:
    RETURN_EXCEPT_PRICE_OF_DELIVERY = "return except price of delivery"
    SENDER_BY_CASH = "sender by cash"
    RECIPIENT_BY_CASH = "recipient by cash"
    ONLINE_BY_CARD = "by card"
    BY_POINTS = "by points"
    FROM_PERSONAL_ACCOUNT_BALANCE = "from personal account balance"


class PaymentReturnForGoodsTypes:
    CARD = "card"
    Y_MONEY = "y money"
    QIWI = "qiwi"


class WhatToDeliverOptions:
    CUSTOM = "Свое значение"
    DOCUMENTS = "Документы"
    SURPRISE = "Сюрприз"
    FRAGILE = "Хрупкий груз"
    HUGE = "Груз >100 см"
    ANOTHER = "Другое"

class CityOfDeliveryOptions:
    MOSCOW = "Москва"
    SAINT_PETERSBURG = "Санкт-Петербург"
    YEKATERINBURG = "Екатеринбург"
    KRASNODAR = "Краснодар"
    CHELYABINSK = "Челябинск"
    N_NOVGOROD = "Нижний Новгород"
    KAZAN = "Казань"

class StartTimeOptions:
    LEAVE_DEFAULT_VALUE = None
    OPTION_DOESNT_MATTER = "00:00"
    OPTION_00_30 = "00:30"
    OPTION_01_00 = "01:00"
    OPTION_01_30 = "01:30"
    OPTION_02_00 = "02:00"
    OPTION_02_30 = "02:30"
    OPTION_03_00 = "03:00"
    OPTION_03_30 = "03:30"
    OPTION_04_00 = "04:00"
    OPTION_04_30 = "04:30"
    OPTION_05_00 = "05:00"
    OPTION_05_30 = "05:30"
    OPTION_06_00 = "06:00"
    OPTION_06_30 = "06:30"
    OPTION_07_00 = "07:00"
    OPTION_07_30 = "07:30"
    OPTION_08_00 = "08:00"
    OPTION_08_30 = "08:30"
    OPTION_09_00 = "09:00"
    OPTION_09_30 = "09:30"
    OPTION_10_00 = "10:00"
    OPTION_10_30 = "10:30"
    OPTION_11_00 = "11:00"
    OPTION_11_30 = "11:30"
    OPTION_12_00 = "12:00"
    OPTION_12_30 = "12:30"
    OPTION_13_00 = "13:00"
    OPTION_13_30 = "13:30"
    OPTION_14_00 = "14:00"
    OPTION_14_30 = "14:30"
    OPTION_15_00 = "15:00"
    OPTION_15_30 = "15:30"
    OPTION_16_00 = "16:00"
    OPTION_16_30 = "16:30"
    OPTION_17_00 = "17:00"
    OPTION_17_30 = "17:30"
    OPTION_18_00 = "18:00"
    OPTION_18_30 = "18:30"
    OPTION_19_00 = "19:00"
    OPTION_19_30 = "19:30"
    OPTION_20_00 = "20:00"
    OPTION_20_30 = "20:30"
    OPTION_21_00 = "21:00"
    OPTION_21_30 = "21:30"
    OPTION_22_00 = "22:00"
    OPTION_22_30 = "22:30"
    OPTION_23_00 = "23:00"
    OPTION_23_30 = "23:30"


class EndTimeOptions:
    LEAVE_DEFAULT_VALUE = None
    OPTION_DOESNT_MATTER = "23:59"
    OPTION_01_00 = "01:00"
    OPTION_01_30 = "01:30"
    OPTION_02_00 = "02:00"
    OPTION_02_30 = "02:30"
    OPTION_03_00 = "03:00"
    OPTION_03_30 = "03:30"
    OPTION_04_00 = "04:00"
    OPTION_04_30 = "04:30"
    OPTION_05_00 = "05:00"
    OPTION_05_30 = "05:30"
    OPTION_06_00 = "06:00"
    OPTION_06_30 = "06:30"
    OPTION_07_00 = "07:00"
    OPTION_07_30 = "07:30"
    OPTION_08_00 = "08:00"
    OPTION_08_30 = "08:30"
    OPTION_09_00 = "09:00"
    OPTION_09_30 = "09:30"
    OPTION_10_00 = "10:00"
    OPTION_10_30 = "10:30"
    OPTION_11_00 = "11:00"
    OPTION_11_30 = "11:30"
    OPTION_12_00 = "12:00"
    OPTION_12_30 = "12:30"
    OPTION_13_00 = "13:00"
    OPTION_13_30 = "13:30"
    OPTION_14_00 = "14:00"
    OPTION_14_30 = "14:30"
    OPTION_15_00 = "15:00"
    OPTION_15_30 = "15:30"
    OPTION_16_00 = "16:00"
    OPTION_16_30 = "16:30"
    OPTION_17_00 = "17:00"
    OPTION_17_30 = "17:30"
    OPTION_18_00 = "18:00"
    OPTION_18_30 = "18:30"
    OPTION_19_00 = "19:00"
    OPTION_19_30 = "19:30"
    OPTION_20_00 = "20:00"
    OPTION_20_30 = "20:30"
    OPTION_21_00 = "21:00"
    OPTION_21_30 = "21:30"
    OPTION_22_00 = "22:00"
    OPTION_22_30 = "22:30"
    OPTION_23_00 = "23:00"
    OPTION_23_30 = "23:30"


# ...