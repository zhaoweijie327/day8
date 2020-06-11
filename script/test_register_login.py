# 导包
import logging
import unittest
import requests
from parameterized import parameterized

from day8.api.login_api import Login_Api
from day8.api.register_api import Register_Api
from day8.app import BASE_DIR
from day8.utiles import read_build


# 创建测试类
class Test_Register_Login(unittest.TestCase):

    # 创建类级别方法
    @classmethod
    def setUpClass(cls):
        # 实例化Session对象
        cls.session = requests.Session()
        # 实例化Register_Api对象
        cls.register = Register_Api()
        # 实例化 Login_Api对象
        cls.login = Login_Api()

    # 创建类级别销毁方法
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 测试注册成功
    @parameterized.expand(read_build(BASE_DIR + '/data/register_login.json',"register"))
    def test_01_register(self,username,verify_code,password,password2,status,msg):
        # 获取验证码
        self.register.verify_api(self.session)


        # 获取注册成功
        data = {"username":username,"verify_code":verify_code,"password":password,"password2":password2}
        res = self.register.register_api(self.session,data)
        logging.info("断言结果: {}".format(res.json()))

        self.assertEquals(status,res.json().get("status"))
        self.assertEquals(msg,res.json().get("msg"))

    # 测试登陆成功
    @parameterized.expand(read_build(BASE_DIR + '/data/register_login.json', "login"))
    def test_login(self,username,password,verify_code,status,msg):
        # 获取验证码
        self.login.tp_verify_02_code(self.session)

        # 登陆
        data = {"username":username,"password":password,"verify_code":verify_code,}
        res = self.login.tp_login(self.session,data)
        logging.info("登陆结果：{}".format(res.json()))

        self.assertEqual(status,res.json().get("status"))
        self.assertEqual(msg, res.json().get("msg"))