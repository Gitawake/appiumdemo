from selenium.webdriver import ActionChains
from basedata.base_test_case import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Two_Encapsulation(BaseTestCase):

    # 显式等待方法
    def wait_element(self, lookup, element):
        wait = WebDriverWait(self.driver, 10)
        try:
            if lookup == "class_name":
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, element)))
            elif lookup == "css_selector":
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            elif lookup == "id":
                wait.until(EC.presence_of_element_located((By.ID, element)))
            elif lookup == "link_text":
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, element)))
            elif lookup == "name":
                wait.until(EC.presence_of_element_located((By.NAME, element)))
            elif lookup == "partial_link_text":
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
            elif lookup == "tag_name":
                wait.until(EC.presence_of_element_located((By.TAG_NAME, element)))
            elif lookup == "xpath":
                wait.until(EC.presence_of_element_located((By.XPATH, element)))
            else:
                BaseTestCase.logger.error("没有定义需要的元素参数...")

            BaseTestCase.logger.info("成功等待的元素 ->" + lookup + "：" + element)
        except Exception as e:
            BaseTestCase.logger.error("未等到等待的元素 ->" + lookup + "：" + element + format(e))
            raise

    # 输入内容方法
    def element_input(self, lookup, element, content):
        try:
            if lookup == "class_name":
                self.driver.find_element_by_class_name(element).send_keys(content)
            elif lookup == "css_selector":
                self.driver.find_element_by_css_selector(element).send_keys(content)
            elif lookup == "id":
                self.driver.find_element_by_id(element).send_keys(content)
            elif lookup == "link_text":
                self.driver.find_element_by_link_text(element).send_keys(content)
            elif lookup == "name":
                self.driver.find_element_by_name(element).send_keys(content)
            elif lookup == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).send_keys(content)
            elif lookup == "tag_name":
                self.driver.find_element_by_tag_name(element).send_keys(content)
            elif lookup == "xpath":
                self.driver.find_element_by_xpath(element).send_keys(content)
            else:
                BaseTestCase.logger.error("没有定义需要的元素参数...")

            BaseTestCase.logger.info("成功在 ->" + element + "！输入值：" + content)
        except Exception as e:
            BaseTestCase.logger.info("未能在 ->" + element + "！输入值：" + content + format(e))
            raise

    # 元素点击方法
    def element_click(self, lookup, element):
        try:
            if lookup == "class_name":
                self.driver.find_element_by_class_name(element).click()
            elif lookup == "css_selector":
                self.driver.find_element_by_css_selector(element).click()
            elif lookup == "id":
                self.driver.find_element_by_id(element).click()
            elif lookup == "link_text":
                self.driver.find_element_by_link_text(element).click()
            elif lookup == "name":
                self.driver.find_element_by_name(element).click()
            elif lookup == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).click()
            elif lookup == "tag_name":
                self.driver.find_element_by_tag_name(element).click()
            elif lookup == "xpath":
                self.driver.find_element_by_xpath(element).click()
            else:
                BaseTestCase.logger.error("没有定义需要的元素参数...")

            BaseTestCase.logger.info("成功点击指定元素 ->" + lookup + "：" + element)
        except Exception as e:
            BaseTestCase.logger.info("点击指定元素失败 ->" + lookup + "：" + element + format(e))
            raise

    # 文本清除操作方法
    def Clear_text(self, lookup, element):
        try:
            if lookup == "class_name":
                self.driver.find_element_by_class_name(element).clear()
            elif lookup == "css_selector":
                self.driver.find_element_by_css_selector(element).clear()
            elif lookup == "id":
                self.driver.find_element_by_id(element).clear()
            elif lookup == "link_text":
                self.driver.find_element_by_link_text(element).clear()
            elif lookup == "name":
                self.driver.find_element_by_name(element).clear()
            elif lookup == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).clear()
            elif lookup == "tag_name":
                self.driver.find_element_by_tag_name(element).clear()
            elif lookup == "xpath":
                self.driver.find_element_by_xpath(element).clear()
            else:
                BaseTestCase.logger.error("没有定义需要的元素参数...")

            BaseTestCase.logger.info("成功清除指定元素 ->" + lookup + "：" + element)
        except Exception as e:
            BaseTestCase.logger.info("清除指定元素失败 ->" + lookup + "：" + element + format(e))
            raise

    # 滑动验证码方法
    def Simulated_sliding(self, element):
        button = self.driver.find_element_by_id(element)  # 找到“蓝色滑块”
        action = ActionChains(self.driver)  # 实例化一个action对象
        action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        action.move_by_offset(260, 0).perform()  # 移动滑块
        Two_Encapsulation.wait_element(self, "class", "nc_iconfont btn_ok")
