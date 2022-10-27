import requests
import json

cur_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
currency = {}

class APIException(Exception):
    def __init__(self, message = ''):
        self.message = message
        super().__init__(self.message)

class Currency:
    def __init__(self, Name='', CharCode='', Value=0, Nominal=0):
        self.name = Name
        self.code = CharCode
        self.value = Value
        self.nominal = Nominal

    def read_cur(self, cur):
        self.name = cur['Name']
        self.code = cur['CharCode']
        self.value = float(cur['Value'])
        self.nominal = int(cur['Nominal'])

class Calculate():
    def __init__(self, base = {}, quote = {}, amount = 0):
        self.base = base
        self.quote = quote
        self.amount = amount

    @staticmethod
    def get_price(base, quote, amount):
        result = (base.value*quote.nominal*amount)/(quote.value*base.nominal)
        return result

def renew_values():
    cur_resp =  requests.get(cur_url).json()
    global currency
    for cur in cur_resp['Valute']:
        cur_value = cur_resp['Valute'].get(cur)
        currency[cur] = Currency()
        currency[cur].read_cur(cur_value)
    rub_cur = """{"CharCode": "RUB", "Nominal": 1, "Name": "Рублей", "Value": 1}"""
    currency['RUB'] = Currency()
    currency['RUB'].read_cur(json.loads(rub_cur))

def calculate(cur1, cur2, ammount):
    renew_values()
    try:
        for cur in [cur1, cur2]:
            if cur not in currency:
                message_text = cur + ' валюта не в списке доступных'
                raise APIException(message_text)
        if cur1 == cur2:
            message_text = 'валюты совпадают'
            raise APIException(message_text)
    except APIException as e:
        return str(e)
    else:
        result = Calculate()
        message_text = result.get_price(currency[cur1], currency[cur2], ammount)
    return message_text

