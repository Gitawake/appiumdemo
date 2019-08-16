# -*- coding: utf-8 -*-
import os
from selenium.webdriver import ActionChains
from bin.Inital_Data import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleiumNew(BaseTestCase):

    # 判断元素是否存在
    def if_element(self, wait_time, element_type, element):
        try:
            BaseTestCase.logger.info('判断元素是否存在... --> 元素名称：' + element)
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(ec.presence_of_element_located((element_type, element)))
        except Exception as e:
            BaseTestCase.logger.info('元素不存在')
            BaseTestCase.logger.error(str(e))
            return False
        else:
            BaseTestCase.logger.info('元素存在')
            return True

    # 显式等待方法、断言
    def wait_element(self, wait_time, element_type, element):
        try:
            BaseTestCase.logger.info('查找元素... --> 元素名称：' + element)
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(ec.presence_of_element_located((element_type, element)))
        except Exception as e:
            BaseTestCase.logger.info('查找元素失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('查找元素成功')

    # 输入内容方法
    def input_element(self, element_type, element, content):
        try:
            BaseTestCase.logger.info('向元素发送字符... --> 内容：' + content + '---|--- 元素名称：' + element)
            self.driver.find_element(element_type, element).send_keys(content)
        except Exception as e:
            BaseTestCase.logger.info('发送字符失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('发送字符成功')

    # 元素点击方法
    def click_element(self, element_type, element):
        try:
            BaseTestCase.logger.info('点击元素... --> 元素名称：' + element)
            self.driver.find_element(element_type, element).click()
        except Exception as e:
            BaseTestCase.logger.info('点击元素失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('点击元素成功')

    # 文本清除操作方法
    def clear_element_text(self, element_type, element):
        try:
            BaseTestCase.logger.info('清除元素占位符... --> 元素名称：' + element)
            self.driver.find_element(element_type, element).clear()
        except Exception as e:
            BaseTestCase.logger.info('清除元素占位符失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('清除元素占位符成功')

    # 断言
    def assertion_element(self, result, element):
        try:
            BaseTestCase.logger.info('断言,元素对比... --> 元素名称：' + result + '==' + element)
            self.assertEqual(result, element)
        except Exception as e:
            BaseTestCase.logger.info('断言失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('断言成功')

    # 触发实体按键
    def simulation_menu_key(self, key_code):
        try:
            BaseTestCase.logger.info('触发实体按键... --> 按键代码：' + str(key_code))
            self.driver.keyevent(key_code)
        except Exception as e:
            BaseTestCase.logger.info('触发实体按键失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('触发实体按键成功')

    # 长按实体按键
    def simulation_long_press_menu_key(self, key_code):
        try:
            BaseTestCase.logger.info('长按实体按键... --> 按键代码：' + str(key_code))
            self.driver.long_press_keycode(key_code)
        except Exception as e:
            BaseTestCase.logger.info('长按实体按键失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('长按实体按键成功')

    # 触发实体按键
    def press_keycod(self, key_code):
        try:
            BaseTestCase.logger.info('触发实体按键... --> 按键代码：' + str(key_code))
            self.driver.press_keycode(key_code)
        except Exception as e:
            BaseTestCase.logger.info('触发实体按键失败')
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info('触发实体按键成功')

    # 滑动验证码方法
    def simulated_sliding(self, element):
        button = self.driver.find_element_by_id(element)  # 找到“蓝色滑块”
        action = ActionChains(self.driver)  # 实例化一个action对象
        action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        action.move_by_offset(260, 0).perform()  # 移动滑块
        SeleiumNew.wait_element(self, "class", "nc_iconfont btn_ok")


class InputMethod(BaseTestCase):
    # 'adb shell ime list -s'  # 列出系统现在所安装的所有输入法
    # 'adb shell settings get secure default_input_method'  # 打印系统当前默认的输入法
    # 'adb shell ime set com.android.inputmethod.latin/.LatinIME'  # 切换latin输入法为当前输入法
    # 'adb shell ime set io.appium.android.ime/.UnicodeIME'  # 切换appium输入法为当前输入法
    # 'adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME'  # 切换appium输入法为搜狗输入法oppo版

    # 切换输入法
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
