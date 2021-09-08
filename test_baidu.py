"""
======================
@author:小谢学测试
@time:2021/9/8:16:19
@email:xie7791@qq.com
======================
"""
import pytest
from selenium import webdriver
import time
import allure
@allure.testcase("http://www.baidu.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://www.baidu.com")
    with allure.step(f"输入搜索关键词:{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)

        driver.find_element_by_id("su").click()

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>','Attch with HTML',allure.attachment_type.HTML)
    with allure.step("关闭浏览器"):
        driver.quit()