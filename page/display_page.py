from selenium.webdriver.common.by import By

import page
from base.base_action import BaseAction
class DisplayPage(BaseAction):

        #初始化函数 在类初始化的时候这个init函数会执行
    def __init__(self, driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)
    #点击显示
    def click_textview_display(self):

        self.click_element(page.display_page_textview_show)
    # 点击搜索按钮
    def click_btn_search(self):

        self.click_element(page.display_page_btn_search)
    # 定位到搜索框并输入内容,
    def input_edit_searvh_content(self,content):

        self.input_edit_content(page.display_page_btn_search,content)
    #点击返回按钮
    def click_btn_back(self):
      self.click_element(page.display_page_btn_back)


