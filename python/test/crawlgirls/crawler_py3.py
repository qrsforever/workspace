#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import html.parser
import urllib.request
import os

zhihu_web_prefix = "https://www.zhihu.com/question"
page_question_ids = (
        61235373, # 女生腿好看胸平是一种什么体验
        28481779, # 腿长是一种什么体验
        19671417, # 拍照时怎样摆姿势好看
        20196263, # 女性胸部过大会有哪些困扰与不便
        46458423  # 短发女孩要怎么拍照才性感
        )
bottom_click_times = 3
image_max_count = 200

def main():
    driver = webdriver.Chrome()
    # Scroll to the bottom, and click the "view more" button
    def execute_times(times):
        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element_by_css_selector('button.QuestionMainAction').click()
                time.sleep(1)
            except:
                break
    for qid in page_question_ids:
        print("question id : " + str(qid))
        page = zhihu_web_prefix + "/" + str(qid)
        driver.get(page)
        print(driver.title + " : " + page)
        execute_times(bottom_click_times)
        # Prettify the html file and store raw data file 
        result_raw = driver.page_source
        result_soup = BeautifulSoup(result_raw, 'html.parser')
        # print(result_soup.prettify())
        # Find all <nonscript> nodes and store them
        noscript_nodes = result_soup.find_all('noscript')
        noscript_txt_all = ""
        for noscript in noscript_nodes:
            noscript_txt_all += noscript.get_text() + "\n"
        imgs_all = html.parser.unescape(noscript_txt_all)
        img_soup = BeautifulSoup(imgs_all, 'html.parser')
        img_nodes = img_soup.find_all('img')

        count = 0
        outdir = "image/" + str(qid) 
        if os.path.exists(outdir):
            os.system("rm -rf " + outdir)
        os.makedirs(outdir)
        for img in img_nodes:
            if img.get('src') is not None:
                img_url = img.get('data-original')
                if img_url is not None:
                    urllib.request.urlretrieve(img_url, outdir + "/" + str(count) + ".jpg")
                    count += 1
            if count > image_max_count:
                break

    driver.close()

if __name__ == '__main__':
    main()
