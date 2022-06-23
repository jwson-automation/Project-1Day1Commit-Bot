from telnetlib import X3PAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt


driver = webdriver.Chrome("./chromedriver")

#페이지 접속
driver.get("https://github.com/")
driver.implicitly_wait(100)

#Sign in 버튼 클릭
driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > div.position-relative.mr-3.mb-4.mb-lg-0.d-inline-block > a").click()
driver.implicitly_wait(100)

#id 비밀번호 입력

id = "YOUR ID"
password = "YOUR PASSWORD"

#날짜 함수로 저장

x = str(dt.datetime.now())

#로그인 하기
driver.find_element_by_name('login').send_keys(id)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('password').send_keys(Keys.ENTER)

driver.implicitly_wait(100)

#repositories 접속

driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > span.dropdown-caret").click()

driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > a:nth-child(6)").click()

driver.find_element_by_css_selector("#user-repositories-list > ul > li:nth-child(1) > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a").click()

driver.find_element_by_css_selector("#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > details > summary > span.d-none.d-md-flex.flex-items-center").click()

driver.find_element_by_css_selector("#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > details > div > ul > li:nth-child(3) > form > button").click()

driver.find_element_by_css_selector("#repo-content-pjax-container > div > div > form.js-blob-form > div > div.breadcrumb.d-flex.flex-shrink-0.flex-items-center.px-3.px-sm-6.px-lg-3 > span > input").send_keys(x)

driver.find_element_by_css_selector("#code-editor > div > pre").send_keys("hello, I'm one-day one-commit bot!")

driver.find_element_by_css_selector("#commit-description-textarea").send_keys("오늘도 성공이에요!")

driver.find_element_by_css_selector("#submit-file").click()

time.sleep(10)



