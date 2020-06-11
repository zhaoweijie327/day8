# 创建注册API类
class Register_Api:

    # 初始化
    def __init__(self):
        # 获取验证码url
        self.verify_code = "http://127.0.0.1/index.php?m=Home&c=User&a=verify&type=user_reg"
        # 获取注册接口url
        self.register = "http://127.0.0.1/Home/User/reg.html"

    # 获取验证码接口
    def verify_api(self,session):
        return session.get(url=self.verify_code)

    # 获取注册接口
    def register_api(self,session,jsonDate):
        return session.post(url=self.register,data=jsonDate)