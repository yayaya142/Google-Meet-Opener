from web_api import WebApi
import time
import test






if __name__ == '__main__':
    print("Hello World")
    WebApi.open_web_api()
    time.sleep(6)
    x = WebApi.get_open_web_url_api()
    print("----------")
    print(x)
    
    
