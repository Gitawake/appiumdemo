# -*- coding: utf-8 -*-
from bin.logger_Instance import Logger
from appium import webdriver
import unittest
import time
import os.path


class BaseTestCase(unittest.TestCase):
    # initialize log printing function
    logger = Logger().logger
    logger.info('initialize log printing function')

    def setUp(self):

        try:
            # Start connection with app
            BaseTestCase.logger.info('Start connection with app')
            # If simulator is used, ADB connect 127.0.0.1:62001 under CMD
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '8.1.0',
                'deviceName': 'MV7PAMPNU8IJ7SIV',
                'appPackage': 'com.zsyj.videomake',
                'appActivity': 'com.zsyj.videomake.ui.welcome.SplashActivity',
                'unicodeKeyboard': True,  # Send string using Unicode encoding
                'resetKeyboard': True,  # Hidden keyboard
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(3)
        except Exception as e:
            BaseTestCase.logger.error('Failed to establish connection with app\n({})'.format(e))
            raise
        else:
            BaseTestCase.logger.info('Successfully established connection with app')

    def tearDown(self):

        # Screenshots
        try:
            BaseTestCase.logger.info('Start Screenshots')
            # Determine whether the required folder exists, otherwise create a
            png_dir = os.path.dirname(os.path.abspath('.')) + '/output/png/'
            if not os.path.exists(png_dir):
                os.makedirs(png_dir)
            png_dir = png_dir + time.strftime('%Y-%m-%d-%H-%M-%S') + '.png'
            self.driver.get_screenshot_as_file(png_dir)
        except Exception as e:
            BaseTestCase.logger.error('Screenshots failed\n({})'.format(e))
        else:
            BaseTestCase.logger.info('Screenshots success')

        BaseTestCase.logger.info(
            '---------------------------------------------{}---------------------------------------------'.format(
                str(time.strftime("%Y-%m-%d %H:%M:%S"))))
        self.driver.quit()
