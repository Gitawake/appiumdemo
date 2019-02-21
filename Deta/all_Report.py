import unittest
import time
from Deta import HTMLTestRunner
import os
import yagmail
from Deta import Basic_class

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath('.')) + '/Encapsulation/'

# 判断需要的测试报告文件夹是否存在，否则创建一个
report_dir = os.path.dirname(os.path.abspath('.')) + '/test_report/'
if not os.path.exists(report_dir):
    os.makedirs(report_dir)


def add_case(rule="test*.py"):
    try:
        # 第一步：加载所有的测试用例
        discover = unittest.defaultTestLoader.discover(cur_path,
                                                       pattern=rule,
                                                       top_level_dir=None)
        Basic_class.logger.info("成功加载所有用例>")
        return discover
    except Exception as e:
        Basic_class.logger.error("用例加载失败>" + e)
        raise


def run_case(all_case):
    try:
        # 第二步：执行所有的用例, 并把结果写入HTML测试报告
        now = time.strftime("%Y_%m_%d_%H_%M_%S")

        report_path = report_dir + now + "_result.html"
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
        # 第三步：获取最新的测试报告
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
        # 第四步：使用yagmail库发送最新的测试报告内容
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
    report_file = get_report_file(report_dir)  # 3获取最新的测试报告
    send_yagmail(report_file)  # 4最后一步发送报告
