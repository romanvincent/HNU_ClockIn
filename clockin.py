# -*- coding: utf-8 -*-

from selenium import webdriver
import time



options = webdriver.ChromeOptions()
options.binary_location = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'  #指定你的浏览器位置





while True:
	wd = webdriver.Chrome(r'c:\driver80\Chromedriver.exe'),options=options)   #指定你的Chromedriver位置。

	wd.get('http://127.0.0.1/app')
	wd.implicitly_wait(20)
	username = wd.find_element_by_css_selector('#app > div > div.login-content > div:nth-child(1) > input[type=text]')
	username.send_keys("你的学号")
	password =  wd.find_element_by_css_selector('#app > div > div.login-content > div:nth-child(2) > input[type=password]')
	password.send_keys("你的密码")
	wd.find_element_by_css_selector('#app > div > div.login-content > button').click()

	time.sleep(10)

	# 登陆模块完成
	div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div.template-content-list.location > div.van-cell.van-cell--clickable > div.van-cell__value > span')
	changelocation='document.querySelector("#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div.template-content-list.location > div.van-cell.van-cell--clickable > div.van-cell__value > span").innerHTML = "LALALA"'
	wd.execute_script(changelocation)

	detail = wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div.template-content-list.location > div.van-cell.van-field > div.van-cell__value > div > input')
	detail.send_keys('你的详细地址')


	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div.van-radio-group > div:nth-child(2)').click()
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div.van-radio-group > div:nth-child(1)').click()
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(5) > div.van-radio-group > div:nth-child(2)').click()
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(6) > div.van-radio-group > div:nth-child(2)').click()
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(7) > div.van-radio-group > div:nth-child(2)').click()
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > div:nth-child(8) > div.van-radio-group > div:nth-child(2)').click()

	time.sleep(5)
	wd.find_element_by_css_selector('#app > div > div.tab-options.van-tabs.van-tabs--line > div.van-tabs__content.van-tabs__content--animated > div > div:nth-child(1) > div > div > div > button').click()


	time.sleep(5)
	wd.quit()
	time.sleep(86400)


