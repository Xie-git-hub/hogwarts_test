"""
======================
@author:小谢学测试
@time:2021/9/7:15:37
@email:xie7791@qq.com
======================
"""
import pytest
def test_04():
    print("test_04")
class Test_pytest():
    def test_01(slef):
        print("pytest_01开始")
        x='this'
        assert 'i' in x
    def test__02(slef):
        print("test_02")
        x = 'hello'
        assert 'e' in x
    def test__03(slef):
        print("test_02")
        a='hello'
        b = 'hello world'
        assert a in b


# def test_case_01(login):
#     print("testcase_01,需要登录")
# def test_case_02():
#     print("testcase_02，不需要登录")
# def test_case_03(login):
#     print("testcase_03，需要登录")


# @pytest.fixture(scope="module")
# def open():
#     print("打开浏览器")
#     yield  #open函数的返回值
#     print("执行teardown")
#     print("关闭浏览器")
# def test_01(open0):
#     print("test_01")
#     raise  NameError
# def test_02(open):
#     print("test_02")
#
# def test_03(open):
#     print("test_03")
#
# if __name__ == '__main__':
#     if __name__ == '__main__':
#         pytest.main()

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("5*7",30)])#传入参数
def test_eval(test_input,expected):
    assert eval(test_input) == expected #断言

@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print("测试数据组合：x:{x},y:{y}")

test_user=['Tom','jerry']
@pytest.fixture(scope="module")
def login(request):
    #接收并传入参数
    user = request.param
    print(f"\n打开首页，登录用户:{user}")
    return user
# #@pytest.mark.skip 可以跳过这条用例，也可以在里面加入跳过条件
# # @pytest.mark.skip("此测试用例不执行")
# #indirect=True 可以把传过来的参数当做函数执行
# # @pytest.mark.xfail (功能为完善时，预定义成功或者失败)
@pytest.mark.parametrize("login",test_user,indirect=True)
def test_login(login):
    a=login
    print(f"测试用例用例中login的返回值{a}")
    assert a != ""

@pytest.mark.search
def test_01():
    print("test_01")
    raise  NameError
@pytest.mark.search
def test_02():
    print("test_02")
@pytest.mark.search
def test_03():
    print("test_03")
@pytest.mark.login
def test_login1():
    print("test_login1")

@pytest.mark.login
def test_login2():
    print("test_login2")
if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main()