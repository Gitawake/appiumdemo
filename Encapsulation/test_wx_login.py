from Deta.Basic_class import Web_test_login


class Xm_sp(Web_test_login):

    def test_wx_login(self):
        Web_test_login.element_click(self, "id", "com.zsyj.wallpaper:id/tv_ignore")

        Web_test_login.element_click(self, "id", "com.zsyj.wallpaper:id/i_mine")

        Web_test_login.element_click(self, "id", "com.zsyj.wallpaper:id/tv_name_my_fragment")

        Web_test_login.element_click(self, "id", "com.zsyj.wallpaper:id/rl_wx_login")

        Web_test_login.wait_element(self, "id", "com.zsyj.wallpaper:id/tv_user_uid")