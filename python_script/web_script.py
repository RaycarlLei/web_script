import logging
import importlib
import subprocess
import os
import time
import random
import csv
import sys
import datetime


try:
    start = int(input("Please enter the start point: "))
    end = int(input("Please enter the end point: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    sys.exit(1)



# 配置日志记录器
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().propagate = False

path = r'C:\Users\12245\OneDrive - University of Florida\Desktop\python_script'


os.chdir(path)

# 检查并安装requests模块
try:
    importlib.import_module('requests')
    logging.info("requests module already installed")
except ImportError:
    logging.info("Installing requests module...")
    subprocess.check_call(['pip3', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info("Requests module installed successfully")

# 检查并安装selenium模块
try:
    importlib.import_module('selenium')
    logging.info("selenium module already installed")
except ImportError:
    logging.info("Installing selenium module...")
    subprocess.check_call(['pip3', 'install', 'selenium'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info("Selenium module installed successfully")

try:
    importlib.import_module('bs4')
    logging.info("bs4 module already installed")
except ImportError:
    logging.info("Installing bs4 module...")
    subprocess.check_call(['pip3', 'install', 'bs4'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info("bs4 module installed successfully")

# try:
#     importlib.import_module('log')
#     logging.info("log module already installed")
# except ImportError:
#     logging.info("Installing log module...")
#     subprocess.check_call(['pip3', 'install', 'log'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     logging.info("log module installed successfully")

try:
    importlib.import_module('win10toast')
    logging.info("win10toast module already installed")
except ImportError:
    logging.info("Installing win10toast module...")
    subprocess.check_call(['pip3', 'install', 'win10toast'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info("win10toast module installed successfully")

from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Title: Task started", "No Context", duration=5, threaded=True)


from bs4 import BeautifulSoup
logging.info('bs4 imported succesful')


# 导入requests模块
import requests
logging.info('requests imported succesful')


# 导入selenium模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from win10toast import ToastNotifier
import sys

logging.info('selenium imported succesful')


log_in_cookie = {
    ".AspNet.Wam": "e00832cd-fcf4-495c-a60b-37d36ffea939%3Alp",
    "ASP.NET_SessionId": "6d76c71d-88dc-4a68-8516-1c14e82e4760",
    "LexisMachineId": "f091f2d4-0226-430d-a168-873dea62dd01",
    "lna2": "MjIxMzYxNWFhYWI4YzlhYmY1ZjAwNzhmYjYyNmVhMDY5NTk4NzI5ZTQyNDI2MzVlZDY4NzY0ZjljODFjY2E3ZTY1NGFiM2U3dXJuOnVzZXI6UEExOTA4NjYyNjMhMTUzMDY3MSwxMDAwMjAyLDE1MTg0OTIsMTUxMjk2OSwxMDAxMDkxLDEwMDAyMDAsMTUxNjgyMywxNTAxMjk3LDEwMDA1ODYsMTAwMDIxNCwxMDAwMjEzLCFub25l",
    "X-LN-Session-TTL": "2023-11-08T03%3A02%3A15Z%2C2023-11-08T00%3A02%3A15Z",
    "LNPAGEHISTORY": "b2674a76-1f08-4f45-b320-add1612558cd%2Cb2674a76-1f08-4f45-b320-add1612558cd"
}

# logged_in_cookie = {
#     'ASP.NET_SessionId': 'e4ec6241-eb5d-4ee3-a909-b52771e7aa42',
#     '.AspNet.Wam': 'bd85948f-67c4-4c3e-82fe-ef361079c132%3Ala',
#     'LexisMachineId': '8a88a445-cca4-439b-b615-74fb1bdb02e0',
#     'LNPAGEHISTORY': '6b43cc83-d9c2-4df1-a106-a81fed2d8172',
#     'lna2': 'M2IzNjI4YWI4ZTZjOGQ1YzRiYWEzOTFmZGZjYWQwZDE0Y2Y1ZjYxNWQ0NjkwOWY2ZGY2M2Y4Mzc3ZjcxNmQzYTY1NGMzYjgzdXJuOnVzZXI6UEExOTA4NjYyNjMhMTUzMDY3MSwxMDAwMjAyLDE1MTg0OTIsMTUxMjk2OSwxMDAxMDkxLDEwMDAyMDAsMTUxNjgyMywxNTAxMjk3LDEwMDA1ODYsMTAwMDIxNCwxMDAwMjEzLCFHVUlEOjA5QUY3MkY3RDhBNzBGQzFFMDYzMDEwMDAwN0Y1RDQy',
#     'X-LN-Session-TTL': '2023-11-09T06%3A53%3A07Z%2C2023-11-09T03%3A53%3A07Z'
# }



my_chrome_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

url = "https://advance.lexis.com/"

options = Options()
# options.add_argument("--headless")  #无头模式
wait_time_2 = random.random() + 0.8
driver = webdriver.Chrome(options=options)

driver.get(url)
driver.delete_all_cookies()
for cookie_name, cookie_value in log_in_cookie.items():
    driver.add_cookie({'name': cookie_name, 'value': cookie_value})

logging.info("正在尝试访问URL: %s", url)
wait = WebDriverWait(driver, 5)
# 获取页面标题
page_title = driver.title
logging.info("成功获得页面标题")

# 获取页面内容
# page_content = driver.page_source
# print("页面内容：", page_content)
# logging.info('成功获取页面内容')








actions = ActionChains(driver)

time.sleep(3)







wait = WebDriverWait(driver, 10)
checkbox_element = wait.until(EC.presence_of_element_located((By.ID, "chkrmflag")))

# 点击复选框
checkbox_element.click()








def enter_username(username):

    # actions.send_keys(Keys.TAB * 11).perform() 
    input_element = driver.find_element(By.NAME, 'userid')
    # actions.move_to_element(input_element).perform()

    input_element.click()# 点击用户名输入框

    

    for char in username:
        # 等待随机时间
        wait_time = random.random()/4

        actions.key_down(char).perform()
        time.sleep(wait_time*0.6)
        actions.key_up(char).perform()
        logging.info("账户输入", char)


        logging.info("等待%s秒" % wait_time)
        time.sleep(wait_time)

    logging.info('用户名输入成功')

enter_username('johnjiang')
time.sleep(wait_time_2)


def enter_password(password):
    input_element = driver.find_element(By.NAME, 'password')
    input_element.click()
    for char in password:
        wait_time = random.random()/4
        actions.key_down(char).perform()
        time.sleep(wait_time*0.5)
        actions.key_up(char).perform()

        logging.info("密码输入",char)

        logging.info("等待%s秒" % wait_time)
        time.sleep(wait_time)
    logging.info('密码输入成功')
    input_element.send_keys(Keys.RETURN)#按回车


enter_password('Gogreen2023')
time.sleep(wait_time_2)

logging.info("输入完毕，可以登录")



time.sleep(wait_time_2)

# 返回上一页
driver.execute_script("window.history.go(-1)")
time.sleep(wait_time_2)
enter_password('Gogreen2023')
# input_element.send_keys(Keys.RETURN)#按回车

# input('/n/n-----------按任意键继续------------/n')

time.sleep(8)
# page_title = driver.title
# logging.info("成功获得登陆后的页面标题")

# 打开url为abc.com的新标签页
search_url = 'https://r3.lexis.com/laprma/FindAPerson.aspx?national=true'
# driver.execute_script("window.open(search_url, '_blank')")


# 保存当前的cookie
# cookies = driver.get_cookies()




def enter_lexis_id(lexis_id):
    actions.send_keys(Keys.BACKSPACE* 11).perform() 
    for char in lexis_id:
        wait_time = random.random()/4 + 0.05
        actions.key_down(char).perform()
        time.sleep(wait_time*0.8)
        actions.key_up(char).perform()

        logging.info("id输入",char)

        logging.info("等待%s秒" % wait_time)
        time.sleep(wait_time)
    input_element.send_keys(Keys.RETURN)#按回车



current_time = datetime.datetime.now().strftime("%H%M")
file_name = f"output_{current_time}_{start}~{end}.csv"

# 创建新写入用CSV文件
with open(file_name, 'w', newline='') as output_file:

    # 创建CSV写入器
    csv_writer = csv.writer(output_file)


    with open('data.csv', 'r') as file:#读取csv文件
    # 创建CSV读取器
        reader = csv.reader(file)
        
        # 跳过标题行
        next(reader)
        
        # 遍历每一行数据
        stop = 0

        # progress_bar = ProgressBar(total=100)

        for row in reader:
            if stop == end:
                break
            if stop <start:
                stop=stop+1
                continue
            stop += 1 
            logging.critical('-----------------Progress: %s of %s----------------' % (stop-800, end-start))
            # progress_bar.update(stop)
            driver.get(search_url)

            # 添加之前保存的cookie
            # for cookie in cookies:
            #     driver.add_cookie(cookie)

            # 刷新页面以应用新的URL和cookie
            # driver.refresh()


            # 等待输入框出现
            wait = WebDriverWait(driver, 20)
            
            # 等待页面加载完成
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # 检查域名是否包含"ValidateCaptcha"字段
            if "ValidateCaptcha" in driver.current_url:
                # 输入任意键继续
                input("Press any key to continue...")
                # 弹出系统弹窗
                toaster = ToastNotifier()
                toaster.show_toast("Meeted Captcha", "Please react", duration=999, threaded=True)

            
            
            input_element = wait.until(EC.presence_of_element_located((By.ID, "MainContent_Did")))

            # 点击输入框
            time.sleep(wait_time_2)
            input_element.click()
            # 获取G列的值
            lexis_id = row[6]
            import re

            # 读取first_name
            def remove_special_characters(string):
                pattern = r'[^a-zA-Z\s]'  # 匹配非字母和非空格的字符
                cleaned_string = re.sub(pattern, '', string)
                return cleaned_string

            first_name = remove_special_characters(row[2].upper())


            logging.info("\nlexis_id: ",lexis_id)
            
            enter_lexis_id(lexis_id)
            wait = WebDriverWait(driver, 10)
            time.sleep(wait_time_2*2)

            try:
                element = driver.find_element(By.PARTIAL_LINK_TEXT, first_name)
                logging.info("Link element with first name '%s' is found" % first_name)
                element.click()
            except NoSuchElementException:
                row[10] = 'No Name'
                csv_writer.writerow(row)
                logging.info("Link element with first name '%s' not found" % first_name)
                continue

            logging.info('搜索名字完成')

            wait = WebDriverWait(driver, 10)
            time.sleep(1.1)



            # 全局搜索name = Professional Licenses
            # 如果没有，csv记录0
            # 如果有，点击链接
            
            try:
                element = driver.find_element(By.XPATH, "//a[contains(text(), 'Professional Licenses')]")
                if element:
                    logging.info("  Professional Licenses is found")
                    wait = WebDriverWait(driver, 10)

                    # 等待元素可见
                    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Professional Licenses')]")))

                    # 检查元素是否可点击
                    if element.is_enabled():
                        try:
                            # 尝试直接点击元素
                            element.click()
                        except:
                            # 如果点击失败，使用ActionChains类模拟鼠标操作
                            actions = ActionChains(driver)
                            actions.move_to_element(element).click().perform()
                    else:
                        # 如果元素不可点击，等待一段时间后再尝试点击
                        time.sleep(2)
                        element.click()
                    wait = WebDriverWait(driver, 10)

                    # 全局搜ACCOUNTANT，如有csv记录1
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'ACCOUNTANCY') or contains(text(), 'ACCOUNTANT')]")
                    if element:
                        logging.info(" ACCOUNTANT is found")
                        row[10] = 'A1'
                        csv_writer.writerow(row)

                    


                else:
                    logging.info("!!! Professional Licenses is not found!!!")
                    row[10] = 'P0'
                    csv_writer.writerow(row)

            except NoSuchElementException:
                logging.info("!!! ACCOUNTANT is not found!!!")

                try:
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'CPA')]")
                    if element:
                        logging.info(first_name+ "`s CPA is found")
                        row[10] = 'C1'
                        csv_writer.writerow(row)
                except:
                        logging.info("!!! CPA is not found!!!")
                        row[10] = 'AC00'
                        csv_writer.writerow(row)











                # logging.info("%s!!! Element not found!!!", first_name)
                # row[10] = 'E0'
                # csv_writer.writerow(row)









            # element = driver.find_element(By.PARTIAL_LINK_TEXT, "Professional Licenses")
            # if element:
            #     logging.info(first_name, "  Professional Licenses is found")
            #     element.click()
            #     time.sleep(3)

            #     # 全局搜ACCOUNTANT，如有csv记录1
            #     element = driver.find_element(By.PARTIAL_LINK_TEXT, "ACCOUNTANT")
            #     if element:
            #         logging.info(first_name, " ACCOUNTANT is found")
            #         row[10] = 'A1'
            #         csv_writer.writerow(row)
                    
            #     else:
            #         logging.info(first_name, "!!! ACCOUNTANT is not found!!!")
            #         element = driver.find_element(By.PARTIAL_LINK_TEXT, "CPA")
            #         if element:
            #             logging.info(first_name+ "`s CPA is found")
            #             row[10] = 'C1'
            #             csv_writer.writerow(row)
                    
            #         else:
            #             logging.info(first_name, "!!! CPA is not found!!!")
            #             row[10] = 'AC0'
            #             csv_writer.writerow(row)
                        
            # else:
            #     logging.info(first_name, "!!! Professional Licenses is not found!!!")
            #     row[10] = 'P0'
            #     csv_writer.writerow(row)
                

        



            # try:
            #     element = driver.find_element(By.PARTIAL_LINK_TEXT, "Professional Licenses")
            #     logging.info("Professional Licenses is found")
            #     element.click()
            # except NoSuchElementException:
            #     logging.info("!!! Professional Licenses is not found!!!")
            #     row[10] = 'P0'
            #     csv_writer.writerow(row)
            #     break

                

            # try:# 全局搜ACCOUNTANT，如有csv记录1
            #         element = driver.find_element(By.PARTIAL_LINK_TEXT, "ACCOUNTANT")
            #         logging.info("ACCOUNTANT is found")
            #         row[10] = 'A1'
            #         csv_writer.writerow(row)
            #         break

                    
            # except NoSuchElementException:
            #     logging.info("!!! ACCOUNTANT is not found!!!")

        
            #     try:# 全局搜CPA,如有csv记录1
            #         element = driver.find_element(By.PARTIAL_LINK_TEXT, "CPA")
            #         logging.info("CPA is found")
            #         row[10] = 'C1'
            #         csv_writer.writerow(row)
            #         break
                
            #     except NoSuchElementException:
            #         logging.info("!!! CPA is not found!!!")
            #         row[10] = 'C0'
            #         csv_writer.writerow(row)
            #         break

            #     row[10] = 'A0'
            #     csv_writer.writerow(row)


toaster = ToastNotifier()
toaster.show_toast("Title: Task Completed", "No Context", duration=9999, threaded=True)
sys.exit()

        



        

#         # csv记录0

#         # 点击<input type="image" name="ctl00$MainContent$resultsToolbar$deliveryDisk" id="MainContent_resultsToolbar_deliveryDisk" class="deliveryToolbar" controlid="deliveryDisk" title="Download Documents" src="/laprma/images/LexisAdvance/download.gif" alt="Download Documents" align="absmiddle" style="visibility: visible;">
#         # 新弹出页面，点ok
#         # 等待10秒
#         # 关闭弹出页面
#         # 返回search_url
#         time.sleep(9.9)



# # 创建新的CSV文件
# with open('output.csv', 'w', newline='') as output_file:
#     # 创建CSV写入器
#     csv_writer = csv.writer(output_file)
    
#     # 写入标题行
#     csv_writer.writerow(['first_name', 'result'])
    
#     with open('data.csv', 'r') as file:
#         # 创建CSV读取器
#         reader = csv.reader(file)
        
#         # 跳过标题行
#         next(reader)
        
#         # 遍历每一行数据
#         for row in reader:
#             driver.get(search_url)
            
#                         # 等待输入框出现
#             wait = WebDriverWait(driver, 10)
#             input_element = wait.until(EC.presence_of_element_located((By.ID, "MainContent_Did")))

#             # 点击输入框
#             input_element.click()
#             # 获取G列的值
#             lexis_id = row[6]
#             first_name = row[3].upper()
#             logging.info("\nlexis_id: ",lexis_id)
            
#             enter_lexis_id(lexis_id)
#             time.sleep(5.5)
            
#             try:
#                 element = driver.find_element(By.PARTIAL_LINK_TEXT, "Professional Licenses")
#                 logging.info("Professional Licenses is found")
#                 element.click()
#                 try:
#                     element = driver.find_element(By.PARTIAL_LINK_TEXT, "ACCOUNTANT")
#                     logging.info("ACCOUNTANT is found")
#                     row[10] = 'A1'
#                     csv_writer.writerow(row)
                    
#                 except NoSuchElementException:
#                     logging.info("!!! ACCOUNTANT is not found!!!")
                    
#                     try:
#                         element = driver.find_element(By.PARTIAL_LINK_TEXT, "CPA")
#                         logging.info("CPA is found")
#                         row[10] = 'C1'
#                         csv_writer.writerow(row)
                    
#                     except NoSuchElementException:
#                         logging.info("!!! CPA is not found!!!")
#                         row[10] = 'C0'
#                         csv_writer.writerow(row)
                    
#                     row[10] = 'A0'
#                     csv_writer.writerow(row)


#             except NoSuchElementException:
#                 logging.info("!!! Professional Licenses is not found!!!")
#                 row[10] = 'P0'
#                 csv_writer.writerow(row)

            
#             # 其他代码...
            







# wait = WebDriverWait(driver, 5)

# page_title = driver.title
# logging.info("成功获得新页面标题")

# page_content = driver.page_source

# logging.info("页面内容：", page_content)





# input_element = driver.find_element_by_id('MainContent_Did')
# input_element.send_keys('00000000')
# input_element.send_keys(Keys.RETURN)

# response = requests.get(url, headers=my_chrome_headers, cookies=log_in_cookie)
# print(response.status_code)
# print(response.text)

# # button_js = "document.querySelector('#button').click();"

# response = requests.get(url, headers=my_chrome_headers)
# print("install successful")
# print(response.status_code)
# print("request successful")


# driver = webdriver.Chrome()
# driver.get(url)

# driver.execute_script(button_js)

# driver.close()
