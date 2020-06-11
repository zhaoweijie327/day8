# 创建登陆API类
class Login_Api:

    # 初始化
    def __init__(self):
        # 获取登陆验证码url
        self.verify_code = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        # 获取登陆接口
        self.login = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"

    # 获取验证码api
    def tp_verify_02_code(self, session):
        return session.get(url=self.verify_code)

    # 封装登陆接口
    def tp_login(self, session, data):
        return session.post(url=self.login, data=data)