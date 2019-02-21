import unittest
import time
from Deta import HTMLTestRunner
import os
import yagmail
from Deta import Basic_class

# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱


# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath('.')) + '/Encapsulation/'


def add_case(rule="test*.py"):
    try:
        '''第一步：加载所有的测试用例'''
        case_path = cur_path  # 用例文件夹
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern=rule,
                                                       top_level_dir=None)
        print(discover)
        Basic_class.logger.info("成功加载所有用例>")
        return discover
    except Exception as e:
        Basic_class.logger.error("用例加载失败>" + e)
        raise


def run_case(all_case):
    try:
        '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/' + now + "_result.html"
        fp = open(report_path, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')

        # 调用add_case函数返回值
        runner.run(all_case)
        fp.close()
        Basic_class.logger.info("成功把执行结果写入HTML测试报告>")
    except Exception as e:
        Basic_class.logger.error("HTML测试报告生成失败>" + e)
        raise


def get_report_file(report_path):
    try:
        '''第三步：获取最新的测试报告'''
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
        print(u'最新测试生成的报告： ' + lists[-1])
        # 找到最新生成的报告文件
        report_file = os.path.join(report_path, lists[-1])
        Basic_class.logger.info("成功获取最新生成的HTML报告>")
        return report_file
    except Exception as e:
        Basic_class.logger.error("获取最新HTML报告失败>" + e)
        raise


def send_yagmail(report_file):
    try:
        '''第四步：使用yagmail库发送最新的测试报告内容'''
        # 链接邮箱服务器，用户密码自己改掉
        yag = yagmail.SMTP(user="vvvvvvvv@126.com", password="xxxxxxxxx", host="smtp.126.com")
        # 邮箱正文
        contents = ['邮件正文', '用例执行情况：']
        # 给多人发送邮件，发送多个附件。如果只发送1个，就去掉列表。
        yag.send(['8888888@qq.com', '99999999@qq.com'], '邮件主题', contents, report_file)
        Basic_class.logger.info("发送邮箱成功>")
    except Exception as e:
        Basic_class.logger.error("发送邮箱失败>" + e)
        raise


if __name__ == "__main__":
    all_case = add_case()  # 1加载用例
    run_case(all_case)  # 2执行用例
    report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'  # 用例保存文件夹
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    send_yagmail(report_file)  # 4最后一步发送报告
