#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 驱动: http://npm.taobao.org/mirrors/chromedriver

import time
from PIL import Image, ImageEnhance
import pytesseract
from selenium import webdriver

autocaptcha = 0
url = "http://www.cnhtcerp.com/sales/"
#  url = "http://www.cnhtcerp.com/sales/index.aspx#/sales/print_sjd_crystal_BC.aspx"
pic_path = "/tmp/code.png"

# 替换列表
rep = {
        'O':'0',                           
        'I':'1',
        'L':'1',
        'Z':'2',
        'S':'8'
    };

# 二值化函数
def _InitTable(threshold = 140):               
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

def AutoInputCaptcha(driver):
    # 截屏
    driver.save_screenshot(pic_path)

    # 验证码位置
    imgelement = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_Panel1_imgCaptcha-inputEl"]/img') 

    # 获取验证码x,y轴坐标
    location = imgelement.location  

    # 获取验证码的长宽
    size = {'height': 30, 'width': 150} 

    # 截取的位置坐标
    rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) 

    # 打开截图
    img = Image.open(pic_path) 

    # 1. 从截图中再次截取验证码区域
    pic1 = img.crop(rangle)

    # 2. 二值化, 将彩色图像转化为灰度图
    pic2 = pic1.convert('L')

    # 3. 对比度增强
    sharpness = ImageEnhance.Contrast(pic2)
    pic3 = sharpness.enhance(2.0)

    # 4. 二值化, 降噪
    pic4 = pic3.point(_InitTable(), '1') 
    pic4.save(pic_path)

    # 使用image_to_string识别验证码
    codenum = Image.open(pic_path)
    text = pytesseract.image_to_string(codenum, config='-psm 7').strip()

    # 验证码错误处理
    for r in rep:
        text = text.replace(r,rep[r])
    codenum = []
    for c in text:
        if c.isdigit(): 
            codenum.append(c)

    return codenum

def UserLogin(driver):
    if autocaptcha:
        time.sleep(3)
        # 自动识别验证码 (TODO: 大概率识别错误)
        text = AutoInputCaptcha(driver)
        captcha = "".join(text)
        print("Check code number: %s" % captcha)
    else:
        # 手动输入验证码
        captcha = input('please enter the code: ')

    username = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxUserName-inputEl"]')
    password = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxPassword-inputEl"]')
    tcaptcha = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxCaptcha-inputEl"]')

    username.send_keys('cszhanghl')
    password.send_keys('cnhtc4088081')
    tcaptcha.send_keys(captcha)
    
    try:
        loginbtn = driver.find_element_by_xpath('//*[@id="Window1_Toolbar1_btnLogin-btnIconEl"]')
        loginbtn.click()
    except:
        print("error")

def main():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window() 
    driver.refresh()

    # 用户登录
    UserLogin(driver)

    # 打开实物交接单打印id 
    while True:
        try:
            print_sjd_crystal_BC = driver.find_element_by_xpath('//*[@id="ext-gen1156"]/div')
            print_sjd_crystal_BC.click()
            break
        except:
            time.sleep(1)
            print("wait for moment")

    time.sleep(1000)
    driver.quit()


if __name__ == "__main__":
    main()
