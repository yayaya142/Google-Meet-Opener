from web_api import WebApi
from message_api import message_api
import time


if __name__ == '__main__':
    WebApi.open_web_api()
    time.sleep(6)
    url = WebApi.get_open_web_url_api()
    print("----------")
    print(url)
    if (url is None):
        print("No meeting found")
        exit(0)
    
    message_api().send_message(url)