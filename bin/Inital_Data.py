# -*- coding: utf-8 -*-
from bin.logger_Instance import Logger
from appium import webdriver
import unittest
import time
import os.path


class BaseTestCase(unittest.TestCase):
    # 初始化log日志
    logger = Logger().logger
    logger.info("初始化log打印功能...")

    def setUp(self):
        try:
            BaseTestCase.logger.info('正在与app建立session...')
            # appium初始化参数，CMD下：adb connect 127.0.0.1:62001
            desired_caps = {'platformName': "Android",
                            'platformVersion': '8.1.0',
                            'deviceName': 'MV7PAMPNU8IJ7SIV',
                            'appPackage': 'com.zsyj.videomake',
                            'appActivity': 'com.zsyj.videomake.ui.welcome.SplashActivity',
                            'unicodeKeyboard': True,  # 使用Unicode编码方式发送字符串
                            'resetKeyboard': True,  # 隐藏键盘
                            }

            # 建立 session
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        except Exception as e:
            BaseTestCase.logger.error('app建立session失败 \n' + format(e))
        else:
            BaseTestCase.logger.info('app建立session成功')

        time.sleep(5)

    def tearDown(self):
        # 判断需要的png文件夹是否存在，否则创建一个
        png_dir = os.path.dirname(os.path.abspath('.')) + '/output/png/'
        if not os.path.exists(png_dir):
            os.makedirs(png_dir)

        # 截取运行结果图片
        try:
            BaseTestCase.logger.info("屏幕截图中...")
            now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file(png_dir + now + ".png")

        except Exception as e:
            BaseTestCase.logger.info("屏幕截图失败")
            BaseTestCase.logger.error(str(e))
        else:
            BaseTestCase.logger.info("屏幕截图成功")

        # 单个用例执行完毕后关闭app
        BaseTestCase.logger.info('******************************' +
                                 str(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))) +
                                 '******************************')
        self.driver.quit()
