import logging
from logging import handlers
import os

# 定义获取到当前目录的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 创建日志
def init_logging():
    # 创建日志器对象
    logger = logging.getLogger()
    # 创建日志级别
    logger.setLevel(level=logging.INFO)
    # 创建处理器（按时间划分日志）
    lht = logging.handlers.TimedRotatingFileHandler(BASE_DIR + '/log/register_login.log',
                                                    when='midnight',interval=1,backupCount=2)
    ls = logging.StreamHandler()
    # 创建格式化器对象
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt_name)
    # 给处理器设置格式化器
    lht.setFormatter(formatter)
    # 给日志器添加处理器
    logger.addHandler(lht)
    logger.addHandler(ls)