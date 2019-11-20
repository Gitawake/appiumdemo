# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from bin.seleium_package import SeleiumNew, InputMethod


class Qzz(SeleiumNew, InputMethod):

    # 初始化启动app
    def mtest_qzz_Initialization(self):

        # 判断权限使用弹框是否存在，存在则点击开启。
        if SeleiumNew.element_is_exist(self, By.ID, 'com.zsyj.videomake:id/btn_dialog_open'):
            SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/btn_dialog_open')

        # 判断储存权限弹框是否存在，存在则点击始终允许。
        if SeleiumNew.element_is_exist(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.element_click(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

        if SeleiumNew.element_is_exist(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.element_click(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

        if SeleiumNew.element_is_exist(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button'):
            SeleiumNew.element_click(self, By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 视频详情页进入视杏模板
    def mtest_qzz_Video_details(self):
        SeleiumNew.element_explicitly_wait(self, 10, By.ID, 'com.zsyj.videomake:id/go_made')

        SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/go_made')

        if SeleiumNew.element_explicitly_wait(self, 5, By.ID, 'com.zsyj.videomake:id/layout_we_chat_login'):
            SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/layout_we_chat_login')
        elif SeleiumNew.element_explicitly_wait(self, 5, By.ID, 'com.zsyj.videomake:id/et_input_code'):
            SeleiumNew.element_send_keys(self, By.ID, 'com.zsyj.videomake:id/et_input_phone', u'13713777056')
            time.sleep(1)
            SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/tv_get_code')
            time.sleep(30)
        time.sleep(1)
        if SeleiumNew.element_explicitly_wait(self, 15, By.ID, 'com.zsyj.videomake:id/tv_next'):
            SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/tv_next')

        if SeleiumNew.element_explicitly_wait(self, 20, By.ID, 'com.zsyj.videomake:id/go_made'):
            SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/go_made')

        SeleiumNew.element_explicitly_wait(self, 10, By.ID, 'com.zsyj.videomake:id/btn_done')

    # 搜索页面测试
    def test_qzz_search(self):

        Qzz.mtest_qzz_Initialization(self)
        time.sleep(2)
        SeleiumNew.entity_key_trigger(self, 5)
        time.sleep(1)
        SeleiumNew.entity_key_trigger(self, 4)

        time.sleep(1)
        SeleiumNew.element_click(self, By.ID, 'com.zsyj.videomake:id/cv_img_home_search')
        time.sleep(1)
        SeleiumNew.element_send_keys(self, By.ID, 'com.zsyj.videomake:id/cv_et_search', u"古风")
        time.sleep(1)
        InputMethod.enableIME(self, 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        time.sleep(3)
        SeleiumNew.entity_key_trigger(self, 66)
        time.sleep(1)
        InputMethod.enableIME(self, 'adb shell ime set io.appium.settings/.UnicodeIME')
        time.sleep(5)
        SeleiumNew.element_explicitly_wait(self, 10, By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        SeleiumNew.element_click(self, By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        time.sleep(2)
        Qzz.mtest_qzz_Video_details(self)





