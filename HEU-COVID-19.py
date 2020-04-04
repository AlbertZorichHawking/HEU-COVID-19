import selenium.webdriver as web
import time
import pyautogui
 
driver = web.Chrome()

driver.get("https://cas.hrbeu.edu.cn/cas/login?service=http%3A%2F%2Fone.hrbeu.edu.cn%2Finfoplus%2Flogin%3FretUrl%3Dhttp%253A%252F%252Fone.hrbeu.edu.cn%252Finfoplus%252Foauth2%252Fauthorize%253Fx_redirected%253Dtrue%2526scope%253Dprofile%252Bprofile_edit%252Bapp%252Btask%252Bprocess%252Bsubmit%252Bprocess_edit%252Btriple%252Bsys_enterprise%2526response_type%253Dcode%2526redirect_uri%253Dhttp%25253A%25252F%25252Fone.hrbeu.edu.cn%25252Ftaskcenter%25252Fwall%25252Fendpoint%25253FretUrl%25253Dhttp%2525253A%2525252F%2525252Fone.hrbeu.edu.cn%2525252Ftaskcenter%2525252Fworkflow%2525252Findex%2526client_id%253D1640e2e4-f213-11e3-815d-fa163e9215bb")
driver.maximize_window()
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('2017024225')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('06200336\n')
time.sleep(3)
driver.get('http://one.hrbeu.edu.cn/infoplus/form/JKXXSB/start')
time.sleep(3)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(1.5)
#第一张图位置坐标
pyautogui.click(725, 822)
time.sleep(1.5)
#第二张
pyautogui.click(113, 163)
time.sleep(1.5)
#第三张
pyautogui.click(1256, 640)
time.sleep(5)
#第四张
pyautogui.click(1151, 623)
time.sleep(2)
driver.quit()