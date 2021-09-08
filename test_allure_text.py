"""
======================
@author:小谢学测试
@time:2021/9/8:16:11
@email:xie7791@qq.com
======================
"""
import pytest
import allure
def test_text():
    allure.attach("这是一个文本","文本",attachment_type=allure.attachment_type.TEXT)
def test_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)