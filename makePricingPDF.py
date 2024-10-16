import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 使用 requests 登入
session = requests.Session()

# 登入的 URL
login_url = 'https://login.ecount.com/Login/'

# 登入所需的資料
payload = {
    'username': 'your_username',  # 替換為你的使用者名稱
    'password': 'your_password'     # 替換為你的密碼
}

# 發送登入請求
response = session.post(login_url, data=payload)

# 檢查登入是否成功
if "login failed" in response.text:
    print("登入失敗")
else:
    print("登入成功")

    # 使用 Selenium 進行瀏覽器自動化
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # 使用已登入的 session cookie（如果需要）
    for cookie in session.cookies:
        driver.add_cookie({'name': cookie.name, 'value': cookie.value})

    # 開啟指定網站
    driver.get("https://login.ecount.com/Login/#menuType=4&menuSeq=487&groupSeq=30&prgId=E040202&depth=4")  # 替換為你需要訪問的頁面

    # 模擬其他操作，例如填寫表單
    time.sleep(5)  # 等待頁面加載
    # 這裡假設你知道表單的 ID 或其他定位方式
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys("example_user")  # 替換為需要填寫的使用者名稱

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("example_password")  # 替換為需要填寫的密碼
    password_field.send_keys(Keys.RETURN)

    # 等待操作完成並抓取 PDF 下載連結
    time.sleep(5)  # 等待頁面加載
    pdf_link = driver.find_element(By.LINK_TEXT, 'Download PDF')  # 替換為實際的 PDF 連結文字
    pdf_link.click()

    # 結束瀏覽器
    driver.quit()
