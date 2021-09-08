"""
======================
@author:小谢学测试
@time:2021/9/8:14:38
@email:xie7791@qq.com
======================
"""
import pytest
import allure
@allure.feature("登录模块")
class TestLogin():
    @allure.story("登陆成功")
    def test_login_succcess(self):
        print("这是登录模块，登陆成功")
    @allure.story("登陆失败")
    def test_login_success_a(self):
        print("这是登录模块a，登陆成功")

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后失败"):
            assert  '1' != 1
            print("登陆失败")
    @allure.story("登陆失败")
    def test_login_failure_a(self):
        print("这是登录，登陆失败")

if __name__ == '__main__':
    pytest.main()