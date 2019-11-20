# -*- coding: utf-8 -*-
import os
from selenium.webdriver import ActionChains
from bin.Inital_Data import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleiumNew(BaseTestCase):

    def element_is_exist(self, element_type, element):
        try:
            BaseTestCase.logger.info('Start to judge whether the element exists({})'.format(element))
            self.driver.find_element(element_type, element)
        except Exception as e:
            BaseTestCase.logger.error('Element not found\n({})'.format(element, str(e)))
            return False
        else:
            BaseTestCase.logger.info('Element found successfully'.format(element))
            return True

    def element_explicitly_wait(self, wait_time, element_type, element):
        try:
            BaseTestCase.logger.info('Wait for element({}) {} seconds'.format(element, wait_time))
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(ec.presence_of_element_located((element_type, element)))
        except Exception as e:
            BaseTestCase.logger.error('Wait for element to timeout\n({})'.format(str(e)))
            return False
        else:
            BaseTestCase.logger.info('Wait for element to succeed')
            return True

    def element_send_keys(self, element_type, element, content):
        try:
            BaseTestCase.logger.info('Send character ({}) to element({})'.format(content, element))
            self.driver.find_element(element_type, element).send_keys(content)
        except Exception as e:
            BaseTestCase.logger.error('Send character failed\n({})'.format(str(e)))
            raise
        else:
            BaseTestCase.logger.info('Send character Success')

    def element_click(self, element_type, element):
        try:
            BaseTestCase.logger.info('Click element({})'.format(element))
            self.driver.find_element(element_type, element).click()
        except Exception as e:
            BaseTestCase.logger.error('Click failed\n({})'.format(str(e)))
            raise
        else:
            BaseTestCase.logger.info('Click Success')

    def element_clear_text(self, element_type, element):
        try:
            BaseTestCase.logger.info('Clear characters in element({})'.format(element))
            self.driver.find_element(element_type, element).clear()
        except Exception as e:
            BaseTestCase.logger.error('Failed to clear characters within an element\n()'.format(str(e)))
            raise
        else:
            BaseTestCase.logger.info('Clear the characters in the element successfully')

    def element_assertion(self, result, element):
        try:
            BaseTestCase.logger.info('断言,元素对比... --> 元素名称：' + result + '==' + element)
            self.assertEqual(result, element)
        except Exception as e:
            BaseTestCase.logger.info('断言失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('断言成功')

    def entity_key_trigger(self, key_code):
        try:
            BaseTestCase.logger.info('触发实体按键... --> 按键代码：' + str(key_code))
            self.driver.keyevent(key_code)
        except Exception as e:
            BaseTestCase.logger.info('触发实体按键失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('触发实体按键成功')

    def entity_key_long_press(self, key_code):
        try:
            BaseTestCase.logger.info('长按实体按键... --> 按键代码：' + str(key_code))
            self.driver.long_press_keycode(key_code)
        except Exception as e:
            BaseTestCase.logger.info('长按实体按键失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('长按实体按键成功')


class InputMethod(BaseTestCase):
    # 'adb shell ime list -s'  # 列出系统现在所安装的所有输入法
    # 'adb shell settings get secure default_input_method'  # 打印系统当前默认的输入法
    # 'adb shell ime set com.android.inputmethod.latin/.LatinIME'  # 切换latin输入法为当前输入法
    # 'adb shell ime set io.appium.android.ime/.UnicodeIME'  # 切换appium输入法为当前输入法
    # 'adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME'  # 切换appium输入法为搜狗输入法oppo版

    def enableIME(self, command):
        try:
            BaseTestCase.logger.info('切换输入法...' + str(command))
            os.system(command)
        except Exception as e:
            BaseTestCase.logger.info('切换输入法失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('切换输入法成功')
