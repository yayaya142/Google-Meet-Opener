import web_api
import time








if __name__ == '__main__':
    print("Hello World")
    web_api.open_web_api()
    time.sleep(6)
    x = web_api.get_open_web_url_api()
    print("----------")
    print(x)
