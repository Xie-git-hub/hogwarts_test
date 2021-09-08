"""
======================
@author:小谢学测试
@time:2021/9/8:10:35
@email:xie7791@qq.com
======================
"""
import pytest
import yaml

class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境ip:",env["test"]) #获取ip
        elif "dev" in env:
            print("开发环境")
            print("这是开发环境的ip:",env["dev"])
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))