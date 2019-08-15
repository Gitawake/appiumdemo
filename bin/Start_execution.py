# -*- coding: utf-8 -*-
from bin.Inital_Data import BaseTestCase
from bin import HTMLTestRunner
import unittest
import time
import os
import yagmail


class FrameEngine(object):
    # 判断需要的测试报告文件夹是否存在，否则创建一个
    report_dir = os.path.dirname(os.path.abspath('.')) + '/output/test_report/'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    @staticmethod
    def add_case(rule="case*.py"):
        try:
            BaseTestCase.logger.info("正在加载测试用例...")
            # 第一步：加载所有的测试用例
            cur_path = os.path.dirname(os.path.abspath('.')) + '/test_case/'  # 当前脚本所在文件真实路径
            discover = unittest.defaultTestLoader.discover(cur_path,
                                                           pattern=rule,
                                                           top_level_dir=None)
        except Exception as e:
            BaseTestCase.logger.info("加载测试用例失败")
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info("成功加载测试用例")
            return discover

    @staticmethod
    def run_case(all_case):
        try:
            BaseTestCase.logger.info("开始生成HTML测试报告...")
            # 第二步：执行所有的用例, 并把结果写入HTML测试报告
            now = time.strftime("%Y_%m_%d_%H_%M_%S")
            report_path = FrameEngine.report_dir + now + "_result.html"
            fp = open(report_path, "wb")
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                   title=u'自动化测试报告,测试结果如下：',
                                                   description=u'用例执行情况：')
            # 调用add_case函数返回值
            runner.run(all_case)
            fp.close()
        except Exception as e:
            BaseTestCase.logger.info("生成HTML测试报告失败")
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info("生成HTML测试报告成功")

    @staticmethod
    def get_report_file(report_path):
        try:
            BaseTestCase.logger.info("正在获取最新HTML测试报告...")
            # 第三步：获取最新的测试报告
            lists = os.listdir(report_path)
            lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
            # 找到最新生成的报告文件
            case_file = os.path.join(report_path, lists[-1])
        except Exception as e:
            BaseTestCase.logger.info("获取最新HTML测试报告失败")
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info("获取最新HTML测试报告成功 -->" + lists[-1])
            return case_file

    @staticmethod
    def send_yagmail(case_file):
        try:
            BaseTestCase.logger.info("正在发送邮箱...")
            # 第四步：使用yagmail库发送最新的测试报告内容
            # 链接邮箱服务器，用户密码自己改掉
            yag = yagmail.SMTP(user="v_dennis@126.com", password="xx", host="smtp.126.com")
            # 邮箱正文
            contents = ['邮件正文', '用例执行情况：']
            # 给多人发送邮件，发送多个附件。如果只发送1个，就去掉列表。
            yag.send(['725365654@qq.com', '392274534@qq.com'], '邮件主题', contents, case_file)

        except Exception as e:
            BaseTestCase.logger.info("发送邮件失败")
            BaseTestCase.logger.error(str(e))
            raise
        else:
            BaseTestCase.logger.info("发送邮件成功")


if __name__ == "__main__":
    case = FrameEngine.add_case()  # 1加载用例
    FrameEngine.run_case(case)  # 2执行用例
    file = FrameEngine.get_report_file(FrameEngine.report_dir)  # 3获取最新的测试报告
    # FrameEngine.send_yagmail(file)  # 4最后一步发送报告
