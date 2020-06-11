#  导包
import time
import unittest

from BeautifulReport import BeautifulReport
from day8.app import BASE_DIR


# 创建测试套件
loader = unittest.TestLoader().discover(BASE_DIR + "/script",pattern="test*.py")

# 定义报告名称
file_name = "repost.html"

# 实例化BeautifulReport的实例运行并生成测试报告
BeautifulReport(loader).report(filename=file_name,description="接口测试报告",log_path=BASE_DIR + "/report")