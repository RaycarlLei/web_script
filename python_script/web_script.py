import logging
import requests
from selenium import webdriver

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    logging.info("Import successful")
except ImportError:
    logging.error("Failed to import necessary modules")


# log_in_cookie = ".AspNet.Wam=e00832cd-fcf4-495c-a60b-37d36ffea939%3Alp; ASP.NET_SessionId=6d76c71d-88dc-4a68-8516-1c14e82e4760; LexisMachineId=f091f2d4-0226-430d-a168-873dea62dd01; lna2=MjIxMzYxNWFhYWI4YzlhYmY1ZjAwNzhmYjYyNmVhMDY5NTk4NzI5ZTQyNDI2MzVlZDY4NzY0ZjljODFjY2E3ZTY1NGFiM2U3dXJuOnVzZXI6UEExOTA4NjYyNjMhMTUzMDY3MSwxMDAwMjAyLDE1MTg0OTIsMTUxMjk2OSwxMDAxMDkxLDEwMDAyMDAsMTUxNjgyMywxNTAxMjk3LDEwMDA1ODYsMTAwMDIxNCwxMDAwMjEzLCFub25l; X-LN-Session-TTL=2023-11-08T03%3A02%3A15Z%2C2023-11-08T00%3A02%3A15Z; LNPAGEHISTORY=b2674a76-1f08-4f45-b320-add1612558cd%2Cb2674a76-1f08-4f45-b320-add1612558cd"



# my_chrome_headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# url = "https://advance.lexis.com/publicrecordshome?crid=6dc59747-d419-4699-aca0-7431c6605fde&cbc=0"

# # button_js = "document.querySelector('#button').click();"

# response = requests.get(url, headers=my_chrome_headers)
# print("install successful")
# print(response.status_code)
# print("request successful")


# driver = webdriver.Chrome()
# driver.get(url)

# driver.execute_script(button_js)

# driver.close()
