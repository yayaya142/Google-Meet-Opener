import requests
import json

class message_api:
    def __init__(self):
        secrets = self.get_secret_from_json()
        self.__token = secrets['token']
        self.__chat_id = secrets['chat_id']

    def send_message(self, message):
        telegram_api().send_message(self.__token, self.__chat_id, message)
        
        
    @staticmethod
    def get_secret_from_json():
        with open('secret.json', 'r') as f:
            data = json.load(f)
        return data
        
        
class telegram_api:
        PREFIX = "https://api.telegram.org/bot"
        def send_message(self, token, chat_id, message):
            url = f"{self.PREFIX}{token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url)
        
        