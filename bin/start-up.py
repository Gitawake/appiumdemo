# -*- coding: utf-8 -*-
from bin.Main import BaseTestCase
from bin.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os
import yagmail

if __name__ == '__main__':

    try:
        case_name = "case*.py"
        cur_path = os.path.dirname(os.path.abspath('.')) + '/test_case/'  # 当前脚本所在文件真实路径
        BaseTestCase.logger.info('Start loading case named ({}) in folder({})'.format(case_name, cur_path))
        discover = unittest.defaultTestLoader.discover(cur_path,
                                                       pattern=case_name,
                                                       top_level_dir=None)
    except Exception as e:
        BaseTestCase.logger.error('Test case loading failed\n({})'.format(str(e)))
        raise
    else:
        BaseTestCase.logger.info("Test case loaded successfully")

    try:
        BaseTestCase.logger.info('Start recording test report')
        now = time.strftime('%Y-%m-%d-%H-%M-%S')
        report_dir = os.path.dirname(os.path.abspath('.')) + '/output/test_report/'
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        report_path = report_dir + now + "-result.html"
        fp = open(report_path, "wb")
        runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告：', description=u'用例执行情况：')
        runner.run(discover)
        fp.close()
    except Exception as e:
        BaseTestCase.logger.error('Test report record failed\n({})'.format(str(e)))
        raise
    else:
        BaseTestCase.logger.info('Test report recorded successfully({})'.format(report_path))

    # try:
    #     BaseTestCase.logger.info('Start sending test report ({}) to mailbox'.format(report_path))
    #     yag = yagmail.SMTP(user="xxx", password="xxx", host="smtp.126.com")
    #     contents = ['邮件正文', '用例执行情况：']
    #     Addressee = ['xx@qq.com', 'xxx@qq.com']
    #     yag.send(Addressee, '邮件主题', contents, report_path)
    #
    # except Exception as e:
    #     BaseTestCase.logger.error('Failed to send mail\n()'.format(str(e)))
    #     raise
    # else:
    #     BaseTestCase.logger.info('Successfully test the test report to {} mailbox'.format(Addressee))
