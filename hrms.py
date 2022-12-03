import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from cryptography.fernet import Fernet
from os.path import exists as file_exists
from selenium.webdriver.chrome.options import Options



###Input credentials
username = password = savecredential = ""
useprevious = False
# showbrowser = input("Hiện trình duyệt lúc chạy script (mặc định Y | N): ")
if file_exists('secret.txt')==False:
    username = input('Nhập tài khoản (evncpc\\taikhoan): ')
    password = getpass.getpass('Nhập mật khẩu: ')
    savecredential = input("Lưu mật khẩu cho lần chạy tiếp theo (mặc định Y | N): ")
    if savecredential.upper() == "Y" or savecredential == "":
        try:
            print("Saving password to file")
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encuname = fernet.encrypt(username.encode())
            encpasswd = fernet.encrypt(password.encode())
            f = open("secret.txt",'w')
            f.write(str(key,encoding='utf-8'))
            f.write('\n')
            f.write(str(encuname,encoding='utf-8'))
            f.write('\n')
            f.write(str(encpasswd,encoding='utf-8'))
            f.write('\n')
            f.close()
            print('Password saved!')
        except:
            print("Error: Failed to save password")

else:
    try:
        print("Using previous password")
        f = open("secret.txt",'r')
        lines = f.readlines()
        if len(lines)==3:
            fernet = Fernet(str(lines[0]))
            username = fernet.decrypt(str(lines[1])).decode()
            password = fernet.decrypt(str(lines[2])).decode()
            print("Password read success!")
            useprevious = True
        else:
            print("Somethings went wrong with password file")
            username = password = ""
        f.close()
    except:
        f.close()
        print("Error: Reading password failed")

if username!="" and password!= "":
    try:
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome()
        # if showbrowser.upper() == "Y" or showbrowser == "":
        #     options = Options()
        #     options.add_argument("--headless")
        #     driver = webdriver.Chrome(options=options)
        driver.get("https://hrms.cpc.vn")
        try:
            uname = driver.find_element(by=By.NAME,value="j_username")
            uname.send_keys(username)
            passwd = driver.find_element(by=By.NAME, value="j_password")
            passwd.send_keys(password)
            try:
                submit_button = driver.find_element(by=By.CLASS_NAME, value="z-button")
                submit_button.click()
                try:
                    logout_button1 = driver.find_element(by=By.CLASS_NAME, value="navbar-profile")
                    logout_button1.click()
                    logout_button = driver.find_element(by=By.CLASS_NAME, value="fa-sign-out")
                    logout_button.click()
                    driver.quit()
                    time.sleep(3)
                except:
                    print("Logout button exception")
                    driver.quit()
                    time.sleep(3)
            except:
                print("Submit button exception")
        except:
            print("Exception Handled")
            driver.quit()
            time.sleep(3)
    except:
        print("Web Driver Exception")
    
else:
    print("Blank username or password")