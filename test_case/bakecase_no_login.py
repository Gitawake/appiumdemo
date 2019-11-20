from bin.SeleiumPacking import Two_Encapsulation
from bin.Main import BaseTestCase


class No_Login(Two_Encapsulation):

    # 未登录状态下推荐页查看视频并且点击关注
    def test_no_login(self):
        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/i_home')

        Two_Encapsulation.element_click(self, 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]')

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/iv_finger')

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/iv_finger1')

        Two_Encapsulation.element_click(self, 'id', 'com.zsyj.wallpaper:id/iv_gz')

        Two_Encapsulation.wait_element(self, 'id', 'com.zsyj.wallpaper:id/rl_wx_login')

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



