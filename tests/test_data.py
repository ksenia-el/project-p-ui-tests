from tests.selectors_for_test_data import *

class TestData:

    valid_login_credentials_msk_user = [{"+79999991122": "coup39fnB90812"}]

    valid_login_credentials_spb_user = [{"+79997777777": "123456"}]

    # None value stands for "not defined", so that no actions are done on these UI elements
    order_info = [

        # set of test data 1
        {"city_of_delivery": CityOfDeliveryOptions.MOSCOW,
         "sender_address": "г Москва, ул Тверская, д 1",
         "sender_entrance": 8,
         "type_sender_floor": None,
         "sender_apt_or_office": None,
         "sender_phone": "8999888888",
         "pick_up_date": 2,  #  where 1 - is "today", 2 - is "tomorrow" and so on (max value is 7)
         "start_time_of_pick_up": StartTimeOptions.LEAVE_DEFAULT_VALUE,  # so, it was left as it was selected by default
         "end_time_of_pick_up": EndTimeOptions.OPTION_DOESNT_MATTER,  # to select "doesn't matter/не важно" option

         "sender_name": "максим***/////548369043",
         "comment_to_sender_address": None,

         "recipient_address": "г Москва, Пречистенский пер, д 7А",
         "recipient_entrance": "первый",
         "recipient_floor": None,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999888888",
         "receiving_date": 2,
         "start_time_receiving": StartTimeOptions.LEAVE_DEFAULT_VALUE,
         "end_time_receiving": EndTimeOptions.OPTION_23_30,

         "get_payment_for_goods": True,
         "type_of_payment_return_for_goods": PaymentReturnForGoodsTypes.CARD,
         "billing_info_for_return": "+ 78999888888",

         "recipient_name": "максим",
         "comment_to_recipient_address": None,

         "what_to_deliver_type": WhatToDeliverOptions.DOCUMENTS,
         "what_to_deliver_specify": "My docs",  # ! this field should always contain a string-value if in the field above ("what_to_deliver_type")
         #  one of these values was selected before: WhatToDeliverOptions.CUSTOM or WhatToDeliverOptions.ANOTHER
         #  otherwise (if DOCUMENTS, FRAGILE, HUGE, or SURPRISE were selected in "what_to_deliver_type" before), the value here
         #  could be either None (if no text input needed) or a string (to additionally type in input field what specifically will be in a delivery)


         "value_per_item": 100,
         "weight_per_item": 50,
         "quantity": 100,

         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.RETURN_EXCEPT_PRICE_OF_DELIVERY,

         "promocode": "поехал"
         },


        # set of test data 2
        {"city_of_delivery": CityOfDeliveryOptions.MOSCOW,
         "sender_address": "Московская обл, Видное, ул Школьная, д 15",
         "sender_entrance": None,
         "type_sender_floor": "второй",
         "sender_apt_or_office": None,
         "sender_phone": "8999777777",
         "pick_up_date": 2,
         "start_time_of_pick_up": StartTimeOptions.OPTION_16_00,
         "end_time_of_pick_up": EndTimeOptions.OPTION_19_00,

         "sender_name": None,
         "comment_to_sender_address": "вход слева",

         "recipient_address": "Московская обл, Одинцово, деревня Губкино, д 39",
         "recipient_entrance": None,
         "recipient_floor": 3,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999777777",
         "receiving_date": 2,
         "start_time_receiving": StartTimeOptions.OPTION_18_00,
         "end_time_receiving": EndTimeOptions.OPTION_21_00,

         "get_payment_for_goods": False,
         "type_of_payment_return_for_goods": None,
         "billing_info_for_return": None,

         "recipient_name": None,
         "comment_to_recipient_address": "второй подъезд, налево",

         "what_to_deliver_type": WhatToDeliverOptions.SURPRISE,
         "what_to_deliver_specify": None,

         "value_per_item": 1000,
         "weight_per_item": 300,
         "quantity": 50,


         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.SENDER_BY_CASH,

         "promocode": "поехал2"
         },

        #set of test data 3
        {"city_of_delivery": CityOfDeliveryOptions.MOSCOW,
         "sender_address": "Московская обл, Домодедово, деревня Чурилково, ул Зеленая, д 41",
         "sender_entrance": None,
         "type_sender_floor": None,
         "sender_apt_or_office": "Семьдесят",
         "sender_phone": "8989800000",
         "pick_up_date": 3,
         "start_time_of_pick_up": StartTimeOptions.OPTION_23_00,
         "end_time_of_pick_up": EndTimeOptions.OPTION_23_30,

         "sender_name": "evgeniy",
         "comment_to_sender_address": None,

         "recipient_address": "Московская обл, Домодедово, село Ям, ул Центральная, д 109",
         "recipient_entrance": None,
         "recipient_floor": None,
         "recipient_apt_or_office": "Пятнадцать",
         "recipient_phone": "8989800000",
         "receiving_date": 3,
         "start_time_receiving": StartTimeOptions.OPTION_23_00,
         "end_time_receiving": EndTimeOptions.OPTION_23_30,

         "get_payment_for_goods": True,
         "type_of_payment_return_for_goods": PaymentReturnForGoodsTypes.Y_MONEY,
         "billing_info_for_return": "+78989800000",

         "recipient_name": "evgeniy",
         "comment_to_recipient_address": None,

         "what_to_deliver_type": WhatToDeliverOptions.FRAGILE,
         "what_to_deliver_specify": None,

         "value_per_item": 50000,
         "weight_per_item": 15000,
         "quantity": 1,

         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.RECIPIENT_BY_CASH,

         "promocode": None
         },


        # set of test data 5
        {"city_of_delivery": CityOfDeliveryOptions.MOSCOW,
         "sender_address": "г Москва, ул Тверская, д 1",
         "sender_entrance": None,
         "type_sender_floor": None,
         "sender_apt_or_office": None,
         "sender_phone": "8999777777",
         "pick_up_date": 2,
         "start_time_of_pick_up": StartTimeOptions.LEAVE_DEFAULT_VALUE,
         "end_time_of_pick_up": EndTimeOptions.OPTION_DOESNT_MATTER,

         "sender_name": None,
         "comment_to_sender_address": None,

         "recipient_address": "г Москва, Пречистенский пер, д 7А",
         "recipient_entrance": None,
         "recipient_floor": 3,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999777777",
         "receiving_date": 2,
         "start_time_receiving": StartTimeOptions.LEAVE_DEFAULT_VALUE,
         "end_time_receiving": EndTimeOptions.OPTION_19_00,

         "get_payment_for_goods": True,
         "type_of_payment_return_for_goods": PaymentReturnForGoodsTypes.QIWI,
         "billing_info_for_return": "+78999777777",

         "recipient_name": None,
         "comment_to_recipient_address": None,

         "what_to_deliver_type": WhatToDeliverOptions.CUSTOM,
         "what_to_deliver_specify": "Шкаф, посуда, стол, коврик кухонный, хозяйственный инвентарь",

         "value_per_item": 1000,
         "weight_per_item": 300,
         "quantity": 50,

         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.RETURN_EXCEPT_PRICE_OF_DELIVERY,

         "promocode": "поехал2"
         }

    ]

# ...

