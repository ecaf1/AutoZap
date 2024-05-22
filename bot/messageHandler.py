import datetime

import requests


class MessageHandler:
    def __init__(self, api_url) -> None:
        self.api_url = api_url

    def validation_message(self, data):
        if not "messages" in data:
            return False
        elif "@g.us" in data["messages"][0]["chat_id"]:
            return False
        elif data["messages"][0]["type"] != "text":
            return False
        else:
            return True

    def add_mensage(self, data, database):
        if self.validation_message(data):
            phone = data["messages"][0]["from"]
            from_name = data["messages"][0]["from_name"]
            message = data["messages"][0]["text"]["body"]
            recepit_date = data["messages"][0]["timestamp"]
            recepit_date = datetime.datetime.fromtimestamp(recepit_date).strftime(
                "%d-%m-%Y, %H:%M:%S"
            )
            self.check_registration(database, phone, from_name, "Nada")
            database.add_message(phone, message, recepit_date)

    def check_registration(self, database, phone, name, description):
        if not database.check_registration(phone):
            database.creat_user(phone, name, description)

    def send_message(self, phone, message):
        payload = {"typing_time": 0, "to": phone + "@s.whatsapp.net", "body": message}
        headers = {"accept": "application/json", "content-type": "application/json"}
        response = requests.post(self.api_url, json=payload, headers=headers)

    def welcome_message(self, phone):
        message = (
            "Olá, bem-vindo à Total Bike Pro! 🚴‍♂️\n"
            "Estamos aqui para ajudar você com tudo relacionado a bicicletas. Como posso assisti-lo hoje?\n\n"
            "Aqui estão algumas opções que você pode escolher:\n"
            "1️⃣ Consultar nosso catálogo de produtos\n"
            "2️⃣ Solicitar um orçamento para serviços de manutenção\n"
            "3️⃣ Informações sobre entrega e frete\n"
            "4️⃣ Assistência com outras questões\n\n"
            "Você pode responder com o número da opção ou digitar sua pergunta. Estou aqui para ajudar!"
        )
        self.send_message(phone, message)
