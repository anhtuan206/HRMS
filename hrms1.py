import requests
import urllib3
import json
import urllib.parse
import getpass
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def logOut():
    url = "https://hrms.cpc.vn/j_spring_logout"
    payload={}
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
loop = input('Nhập số lần đăng nhập (max 50):')
username = input('Nhập tài khoản (evncpc\\taikhoan): ')
password = getpass.getpass('Nhập mật khẩu: ')
username = urllib.parse.quote(username)
password = urllib.parse.quote(password)

url = "https://hrms.cpc.vn/j_spring_security_check?j_username="+username+"&j_password="+password
payload={}
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded'
}
for i in range(int(loop)):
    if i == 50: break
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    print("Lần",i,":",response)
    time.sleep(3)
    logout = logOut()
    print("Logged out",logout)
else:
    print("Finished!")