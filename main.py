from web_api import WebApi
from message_api import message_api
import pyperclip as pc
import time


if __name__ == '__main__':
    user_select = input("Do you want to open the meeting? (1 if Yes): ")
    if (user_select == "1"):
        WebApi.open_web_api()
        time.sleep(6)
        url = WebApi.get_open_web_url_api()
        print("----------")
        print(url)
        if (url is None):
            print("No meeting found")
            exit(0)
             
        pc.copy(url)
        message_api().send_message(url)
