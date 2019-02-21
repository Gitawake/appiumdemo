import unittest
import time
from appium import webdriver
import os.path
from Deta import Basic_class


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': "Android",
                        'platformVersion': '4.4.2',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.zsyj.wallpaper',
                        'appActivity': 'com.zsyj.wallpaper.ui.welcome.SplashActivity'}

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 建立 session

        time.sleep(5)

    def tearDown(self):
        # 截取运行结果图片
        try:
            now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file((os.path.dirname(os.path.abspath('.')) + '/png/') + now + ".png")
            Basic_class.logger.info("成功保存运行结果截图>")
        except Exception as e:
            Basic_class.logger.error("保存运行结果截图失败>" + e)
        self.driver.quit()
