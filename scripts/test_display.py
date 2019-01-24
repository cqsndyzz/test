import os, sys
sys.path.append(os.getcwd())
from base.read_yaml import read_yaml_data
from page.display_page import DisplayPage
import page
from base.init_driver import init_driver
import pytest

import time

#读取yaml数据
def read_data1():
    data = read_yaml_data('settings.yaml')
    return data.get("send_data")


class TestSetting:
    #初始化driver
    def setup_class(self):
        self.driver = init_driver(page.display_app_package,page.display_app_activity)
        self.displaypage = DisplayPage(self.driver)
    #2初始化DisplayPage 类
        self.display_Page = DisplayPage(self.driver)
    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()



    def test_search_btn(self):
        self.display_Page.click_textview_display()
        # 2.点击搜索按钮
    def test_input_search(self):
        self.display_Page.click_btn_search()
        #3.定位到搜索框 并输入内容
    @pytest.mark.parametrize('content',read_data1())
    def test_input(self,content):
        self.display_Page.input_edit_searvh_content(content)
        #4.点击返回按钮
    def test_click_back_btn(self):
        self.display_Page.click_btn_back()




