from basedata.two_encapsulation import Two_Encapsulation
from basedata.base_test_case import BaseTestCase


class Xm_sps(Two_Encapsulation):

    # QQ登录
    def test_qq_login(self):
        try:
            Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_ignore')
        except Exception as e:
            BaseTestCase.logger.error("没有更新提示..." + format(e))

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/i_mine')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_name_my_fragment')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/rl_qq_login')

        try:
            Two_Encapsulation.element_click(self, 'xpath',
                                            '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button')
        except Exception as e:
            BaseTestCase.logger.error("没有授权按钮，继续查找下一个元素..." + format(e))

        Two_Encapsulation.wait_element(self, 'id', 'com.zsyj.wallpaper:id/tv_user_uid')
        BaseTestCase.logger.info("登录成功...")

    # 微信登录
    def xtest_wx_login(self):
        try:
            Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_ignore')
        except Exception as e:
            BaseTestCase.logger.error("没有更新提示..." + format(e))

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/i_mine')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/tv_name_my_fragment')
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/rl_wx_login')

        try:
            Two_Encapsulation.element_click(self, 'xpath', '')
        except Exception as e:
            BaseTestCase.logger.error("没有授权按钮，继续查找下一个元素..." + format(e))

        Two_Encapsulation.wait_element(self, 'id', 'com.zsyj.wallpaper:id/tv_user_uid')
        BaseTestCase.logger.info("登录成功...")









