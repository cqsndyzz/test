# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By
display_app_package = "com.android.settings"
display_app_activity = ".Settings"

# display_page
display_page_textview_show = (By.XPATH, "//*[contains(@text,'显示')]")
display_page_btn_search = (By.ID, "com.android.settings:id/search")
display_page_edit_search_content = (By.ID, "android:id/search_src_text")
display_page_btn_back = (By.CLASS_NAME, "android.widget.ImageButton")

