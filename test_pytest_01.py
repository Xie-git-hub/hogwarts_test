"""
======================
@author:小谢学测试
@time:2021/9/8:9:58
@email:xie7791@qq.com
======================
"""
import pytest
import yaml
class TestData:
    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))#传入参数
    def test_eval(self,a,b):
        print(a+b)

