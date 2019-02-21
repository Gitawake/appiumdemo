import logging
import os.path
import time


class Logger(object):
    def __init__(self):
        # 创建一个logger
        self.logger = logging.getLogger('bench-server')
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 判断需要的log文件夹是否存在，否则创建一个
        log_dir = os.path.dirname(os.path.abspath('.')) + '/logs/'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_name = log_dir + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
