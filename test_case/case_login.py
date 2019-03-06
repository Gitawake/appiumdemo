from basedata.two_encapsulation import Two_Encapsulation
from basedata.base_test_case import BaseTestCase


class Xm_sps(Two_Encapsulation):

    # 我的页面QQ登录
    def test_qq_login(self):
        try:
            Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_ignore')
        except Exception as e:
            BaseTestCase.logger.error("没有更新提示... \n" + format(e))

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/i_mine')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_name_my_fragment')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/rl_qq_login')

        try:
            Two_Encapsulation.element_click(self, 'class_name', 'android.widget.Button')
        except Exception as e:
            BaseTestCase.logger.error("没有授权按钮，继续查找下一个元素... \n" + format(e))

        try:
            Two_Encapsulation.wait_element(self, 'id', 'com.zsyj.wallpaper:id/tv_user_uid')
            BaseTestCase.logger.info("登录成功...")
        except Exception as e:
            BaseTestCase.logger.error("登录失败... \n" + format(e))

    # 我的页面微信登录
    def xtest_wx_login(self):
        try:
            Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_ignore')
        except Exception as e:
            BaseTestCase.logger.error("没有更新提示... \n" + format(e))

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/i_mine')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_name_my_fragment')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/rl_wx_login')

        try:
            Two_Encapsulation.element_click(self, 'xpath', '')
        except Exception as e:
            BaseTestCase.logger.error("没有授权按钮，继续查找下一个元素... \n" + format(e))

        Two_Encapsulation.wait_element(self, 'id', 'com.zsyj.wallpaper:id/tv_user_uid')
        BaseTestCase.logger.info("登录成功...")









