from basedata.logger import Logger
from appium import webdriver
import unittest
import time
import os.path


class BaseTestCase(unittest.TestCase):
    # 初始化log日志
    logger = Logger().logger
    logger.info("初始化log...")

    def setUp(self):
        try:
            # appium初始化参数，CMD下：adb connect 127.0.0.1:62001
            desired_caps = {'platformName': "Android",
                            'platformVersion': '4.4.2',
                            'deviceName': '127.0.0.1:62001',
                            'appPackage': 'com.zsyj.wallpaper',
                            'appActivity': 'com.zsyj.wallpaper.ui.welcome.SplashActivity'}

            # 建立 session
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

            BaseTestCase.logger.info('成功与app建立session...')
        except Exception as e:
            BaseTestCase.logger.error('与app建立session失败... \n' + format(e))

        time.sleep(5)

    def tearDown(self):
        # 判断需要的png文件夹是否存在，否则创建一个
        png_dir = os.path.dirname(os.path.abspath('.')) + '/png/'
        if not os.path.exists(png_dir):
            os.makedirs(png_dir)

        # 截取运行结果图片
        try:
            now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file(png_dir + now + ".png")

            BaseTestCase.logger.info("成功保存运行结果截图...")
        except Exception as e:
            BaseTestCase.logger.error("保存运行结果截图失败... \n" + format(e))

        # 单个用例执行完毕后关闭app
        BaseTestCase.logger.info('*************************************单元分割线*************************************')
        self.driver.quit()
