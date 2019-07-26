from selenium import webdriver
from public import ElementLocate


class Action:
    # 打开浏览器方法
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("浏览器%s不存在！" % browser)

        self.driver.maximize_window()       # 浏览器最大化

    # 跳转连接方法
    def navigate(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(30)         # 等待30s

    # 输入框输入方法
    def input(self, loc, value):
        ElementLocate.send_keys(self.driver, loc, value)

    # 按钮点击方法
    def click(self, loc):
        pass

    # 断言校验方法
    def verify(self, value):
        pass

    # 关闭浏览器方法
    def close_browser(self):
        pass

    # 点击元素方法
    def click_element(self, loc):
        pass

