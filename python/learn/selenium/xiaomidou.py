#!C:\Users\teresa\AppData\Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-

# 驱动: http://npm.taobao.org/mirrors/chromedriver

# 使用方法 (参考https://blog.csdn.net/tyhj_sf/article/details/74891096）
# 1. 安装chrome浏览器并启动, 在地址栏输入：chrome://settings/help 查看chrome浏览器的版本号
# 2. 把Selenium整个文件放到C:\目录下
# 3. 打开C:\Selenium\notes.txt, 查找对应chrome浏览器对应版本的chromedriver版本号
# 4. 到http://npm.taobao.org/mirrors/chromedriver下载正确的chromedrive， 解压放到C:\Selenium中
# 5. 下载并安装https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
# 6. 配置环境变量Path将%USERPROFILE%\AppData\Local\Programs\Python\Python36\;添加到Path中（具体操作百度一下）
# 7. 修改该文件的最上面一行（默认安装python的话， 只需要将teresa改为你的用户名 
# 8. win + r, 输入cmd， 进入cmd命令行:  python -m pip install -U selenium
# 9. 到C:\Selenium 双击xiaomidou.py
# 10. 在弹出的终端上输入验证码

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#  from PIL import Image, ImageEnhance
#  import pytesseract

#  autocaptcha = 0
debug = 1
url = "http://www.cnhtcerp.com/sales/"
pic_path = "/tmp/code.png"
pdf_path = "C:\Selenium\pdf"
driver_path = "C:\Selenium\chromedriver.exe"

paramstable = {
        'sdate' : '2017-9-1',
        'edate' : '2017-10-11',
        'jxs' : 'ACS2004',
        }

def DebugFindElements(driver, path, attr):
    """
    调试, xpath获取到元素的属性
    """
    if debug:
        items = driver.find_elements_by_xpath(path)
        print("find elements by xpath(%s)" % path)
        i = 1
        for e in items:
            if attr == 'text':
                print("%3d. text = %s" % (i, e.text))
            else:
                print("%3d. attribute[%s] = %s" % (i, attr, e.get_attribute(attr)))
            i += 1

def DelayFindElement(func):
    """
    由于网络加载慢, 需要延时获取元素
    """
    while True:
        try:
            return func()
        except:
            time.sleep(1)
            print("loading...")


# def AutoInputCaptcha(driver):
#     """
#     自动解析验证码
#     """
# 
#     # 替换列表
#     rep = {
#             'O':'0',                           
#             'I':'1',
#             'L':'1',
#             'Z':'2',
#             'S':'8'
#         };
# 
#     # 二值化函数
#     def _InitTable(threshold = 140):               
#         table = []
#         for i in range(256):
#             if i < threshold:
#                 table.append(0)
#             else:
#                 table.append(1)
#     
#         return table
# 
#     # 截屏
#     driver.save_screenshot(pic_path)
# 
#     # 验证码位置
#     imgelement = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_Panel1_imgCaptcha-inputEl"]/img') 
# 
#     # 获取验证码x,y轴坐标
#     location = imgelement.location  
# 
#     # 获取验证码的长宽
#     size = {'height': 30, 'width': 150} 
# 
#     # 截取的位置坐标
#     rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) 
# 
#     # 打开截图
#     img = Image.open(pic_path) 
# 
#     # 1. 从截图中再次截取验证码区域
#     pic1 = img.crop(rangle)
# 
#     # 2. 二值化, 将彩色图像转化为灰度图
#     pic2 = pic1.convert('L')
# 
#     # 3. 对比度增强
#     sharpness = ImageEnhance.Contrast(pic2)
#     pic3 = sharpness.enhance(2.0)
# 
#     # 4. 二值化, 降噪
#     pic4 = pic3.point(_InitTable(), '1') 
#     pic4.save(pic_path)
# 
#     # 使用image_to_string识别验证码
#     codenum = Image.open(pic_path)
#     text = pytesseract.image_to_string(codenum, config='-psm 7').strip()
# 
#     # 验证码错误处理
#     for r in rep:
#         text = text.replace(r,rep[r])
#     codenum = []
#     for c in text:
#         if c.isdigit(): 
#             codenum.append(c)
# 
#     return codenum

def UserLogin(driver):
    # if autocaptcha:
    #     time.sleep(3)
    #     # 自动识别验证码 (TODO: 大概率识别错误)
    #     text = AutoInputCaptcha(driver)
    #     captcha = "".join(text)
    #     print("Check code number: %s" % captcha)
    # else:
    #     # 手动输入验证码
    #     captcha = input('please enter the code: ')
    captcha = input('please enter the code: ')

    username = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxUserName-inputEl"]')
    password = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxPassword-inputEl"]')
    tcaptcha = driver.find_element_by_xpath('//*[@id="Window1_SimpleForm1_tbxCaptcha-inputEl"]')

    username.send_keys('testcszhanghl')
    password.send_keys('testcnhtc4088081123654')
    tcaptcha.send_keys(captcha)
    
    try:
        loginbtn = driver.find_element_by_xpath('//*[@id="Window1_Toolbar1_btnLogin-btnIconEl"]')
        loginbtn.click()
    except:
        print("error")

def ConfigQueryParameters(driver):
    DebugFindElements(driver, '//input[@id]', 'id')
    # 出库日期
    sdate = DelayFindElement(
            lambda: driver.find_element_by_id('Panel0_Panel2_Form2_FormRow21_datePicker_sdate-inputEl'))
    sdate.clear()
    sdate.send_keys(paramstable['sdate'])

    # 终止日期
    edate = DelayFindElement(
            lambda: driver.find_element_by_id('Panel0_Panel2_Form2_FormRow21_datePicker_edate-inputEl'))
    edate.clear()
    edate.send_keys(paramstable['edate'])

    # 经销商21号 
    btn = driver.find_element_by_xpath('//*[@id="ext-gen1066"]')
    btn.click()
    jxslist = DelayFindElement(
            lambda: driver.find_element_by_id('Panel0_Panel2_Form2_FormRow21_DropDownList_jxs-inputEl'))
    items = driver.find_elements_by_xpath('//*[@id="boundlist-1011-listEl"]')[0].text.split('\n')
    for i, e in enumerate(items, 1):
        jxslist.send_keys(Keys.DOWN)    
        jxs = e.split(' ')[0]
        if debug:
            print('%3d. jxs:  %s vs %s' % (i, jxs, paramstable['jxs']))
        if jxs == paramstable['jxs']:
            break
    jxslist.send_keys(Keys.ENTER)

    # 点击查询
    search = driver.find_element_by_id('Panel0_Panel1_toolBar1_ButtonSearch-btnEl')
    search.click() 
    time.sleep(3)


def DownloadDropdownList(driver):
    """
    下载交接单号
    """

    btn = driver.find_element_by_xpath('//*[@id="ext-gen1069"]')
    btn.click()
    sjdlist = DelayFindElement(
            lambda: driver.find_element_by_id('Panel0_Panel2_Form2_FormRow22_DropDownList_sjd-inputEl'))
    items = driver.find_elements_by_xpath('//*[@id="boundlist-1011-listEl"]')[0].text.split('\n')

    for i, e in enumerate(items, 1):
        if debug:
            print('%3d. sjd: %s ' % (i, e))
        # 重新点击表单
        driver.find_element_by_xpath('//*[@id="ext-gen1069"]').click()
        sjdlist = DelayFindElement(
                lambda: driver.find_element_by_id('Panel0_Panel2_Form2_FormRow22_DropDownList_sjd-inputEl'))
        # 修改readonly属性
        js = 'document.getElementById("Panel0_Panel2_Form2_FormRow22_DropDownList_sjd-inputEl").removeAttribute("readonly")'
        driver.execute_script(js)
        try:
            sjdlist.clear()
            sjdlist.send_keys(e)
        except:
           print('error for sjd: %s' % e)
           continue

        # 点击预览
        preview = DelayFindElement(
                lambda: driver.find_element_by_id('Panel0_Panel1_toolBar1_Button_yl-btnEl'))
        preview.click() 
        time.sleep(5) # preview loading...

        # 点击保存
        savebtn = DelayFindElement(
                lambda: driver.find_element_by_id('Panel0_Panel3_contentPanel1_ReportViewer1_ctl06_ctl04_ctl00_ButtonImg'))
        savebtn .click()
        pdf = DelayFindElement(
                lambda: driver.find_element_by_xpath(
                    '//*[@id="Panel0_Panel3_contentPanel1_ReportViewer1_ctl06_ctl04_ctl00_Menu"]/div[2]/a'))
        pdf.click()
        time.sleep(3) # pdf downloading...

        # 重命名
        filename = e.replace('/', '-') + ".pdf"
        src = os.path.join(pdf_path, 'Report.pdf')
        dst = os.path.join(pdf_path, filename)
        os.rename(src, dst)

def main():
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': pdf_path}  
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    driver.get(url)
    driver.maximize_window() 
    driver.refresh()

    # 用户登录
    UserLogin(driver)

    # 跳转到实物交接单打印页iframe
    DebugFindElements(driver, '//*[@href]', 'href')
    print_sjd_crystal_BC = DelayFindElement(
            lambda: driver.find_element_by_xpath('//*[@id="ext-gen1156"]/div'))
    print_sjd_crystal_BC.click()
    driver.switch_to.frame(DelayFindElement(
        lambda: driver.find_element_by_xpath('//iframe[contains(@src,"print_sjd_crystal_BC.aspx")]')))
    
    # 设置查询参数
    ConfigQueryParameters(driver)

    # 下载交接单文档 
    DownloadDropdownList(driver)

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
