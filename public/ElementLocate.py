from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# 重写单一元素的定位方法
def find_element(driver, *loc):
    try:
        element = WebDriverWait(driver, 30).until(lambda driver: driver.find_element(*loc))
    except NoSuchElementException:
        print("页面中没有找到%s元素" % loc)
    else:
        return element


# 重写一组元素的定位方法
def find_elements(driver, *loc):
    try:
        elements = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements(*loc))
    except NoSuchElementException:
        print("页面中没有找到%s元素" % loc)
    else:
        return elements


# 重写send_keys方法: 先定位元素再输入内容
def send_keys(driver, loc, value):
    element = find_element(driver, *loc)    # 定位输入框
    element.clear()     # 先清空输入框
    element.send_keys(value)        # 输入value

# # 重写switch_frame方法
# def switch_frame(driver, loc):
#     return driver.switch_to_frame(loc)


# 调试用
if __name__ == '__main__':
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()
    driver.get('https://uat-doctor.dr-elephant.net/login')
    driver.maximize_window()
    time.sleep(3)
    username = find_element(driver, "xpath", "//*[@id='app']/div/div/div/div/div[3]/form/div[1]/div/div/input")
    password = find_elements(driver, "xpath", "//*[@id='app']/div/div/div/div/div[3]/form/div[2]/div/div/input")

    loc_username = ("xpath", "//*[@id='app']/div/div/div/div/div[3]/form/div[1]/div/div/input")
    send_keys(driver, loc_username, '15221739591')

    loc_password = ("xpath", "//*[@id='app']/div/div/div/div/div[3]/form/div[2]/div/div/input")
    send_keys(driver, loc_password, '739591')

    loc_button = ("xpath", "//*[@id='app']/div/div/div/div/div[3]/form/div[4]/div/button")
    element = find_element(driver, *loc_button).click()
    time.sleep(5)

    # tips = ("xpath", "/html/body/div[3]")
    # element_tip = find_element(driver, *tips)
    # tip_msg = element_tip.text
    # print(tip_msg)

    loc_tab = ("xpath", "//*[@id='app']/div/div/div[2]/div[1]/div[1]/div/div/div/div/ul/li[6]")
    find_element(driver, *loc_tab).click()
    begin_time = ("xpath", "//*[@id='Readmehome']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div[1]/div/input")
    # send_keys(driver, begin_time, '111')
    find_element(driver, *begin_time).click()
    time.sleep(2)
    # begin_time_hour = ("xpath", "//*[@id='Readmehome']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div[2]/div/div/div/div/div/div[1]/ul/li[18]")
    begin_time_hour = ("xpath", "//*[@id='Readmehome']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div[2]/div/div/div/div/div/div[1]/ul/li[16]")
    begin_time_mini = ("xpath", "//*[@id='Readmehome']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div[2]/div/div/div/div/div/div[2]/ul/li[4]")
    find_element(driver, *begin_time_hour).click()
    find_element(driver, *begin_time_mini).click()
    time.sleep(2)
    end_time = ("xpath", "//*[@id='Readmehome']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[4]/div[3]/div/div[1]/div/input")
    try:
        find_element(driver, *end_time).click()
        find_element(driver, *end_time).click()
        time.sleep(10)
    except NoSuchElementException:
        print("找不到元素")


    driver.quit()
