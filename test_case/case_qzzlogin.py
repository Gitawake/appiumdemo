# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from bin.seleium_package import SeleiumNew, InputMethod


class Qzz(SeleiumNew, InputMethod):

    # 初始化启动app
    def mtest_qzz_Initialization(self):

        if SeleiumNew.if_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.click_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

        time.sleep(2)
        SeleiumNew.simulation_menu_key(self, 5)
        time.sleep(1)
        SeleiumNew.simulation_menu_key(self, 4)

        if SeleiumNew.if_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.click_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

        if SeleiumNew.if_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.click_element(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 视频详情页进入视杏模板
    def mtest_qzz_Video_details(self):
        SeleiumNew.wait_element(self, By.ID, 'com.zsyj.videomake:id/go_made')
        SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/go_made')

        if SeleiumNew.if_element(self, By.ID, 'com.zsyj.videomake:id/layout_we_chat_login'):
            SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/layout_we_chat_login')
        elif SeleiumNew.if_element(self, By.ID, 'com.zsyj.videomake:id/et_input_code'):
            SeleiumNew.input_element(self, By.ID, 'com.zsyj.videomake:id/et_input_phone', u'13713777056')
            SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/tv_get_code')
            time.sleep(30)

        if SeleiumNew.if_element(self, By.ID, 'com.zsyj.videomake:id/tv_next'):
            SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/tv_next')

        time.sleep(25)
        SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/go_made')
        SeleiumNew.wait_element(self, By.ID, 'com.zsyj.videomake:id/btn_done')

    # 搜索页面测试
    def test_qzz_search(self):

        Qzz.mtest_qzz_Initialization(self)
        time.sleep(2)
        SeleiumNew.simulation_menu_key(self, 5)
        time.sleep(1)
        SeleiumNew.simulation_menu_key(self, 4)

        time.sleep(1)
        SeleiumNew.click_element(self, By.ID, 'com.zsyj.videomake:id/cv_img_home_search')
        time.sleep(1)
        SeleiumNew.input_element(self, By.ID, 'com.zsyj.videomake:id/cv_et_search', u"古风")
        time.sleep(1)
        InputMethod.enableIME(self, 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        time.sleep(3)
        SeleiumNew.simulation_menu_key(self, 66)
        time.sleep(1)
        InputMethod.enableIME(self, 'adb shell ime set io.appium.settings/.UnicodeIME')
        time.sleep(5)
        SeleiumNew.wait_element(self, By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        SeleiumNew.click_element(self, By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        time.sleep(20)
        Qzz.mtest_qzz_Video_details(self)





