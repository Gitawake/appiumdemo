from basedata.two_encapsulation import Two_Encapsulation


class Xm_sps(Two_Encapsulation):

    def test_qq_login(self):
        Two_Encapsulation.element_click(self, "id", "com.zsyj.wallpaper:id/tv_ignore")

        Two_Encapsulation.element_click(self, "id", "com.zsyj.wallpaper:id/i_mine")

        Two_Encapsulation.element_click(self, "id", "com.zsyj.wallpaper:id/tv_name_my_fragment")

        Two_Encapsulation.element_click(self, "id", "com.zsyj.wallpaper:id/rl_qq_login")

        Two_Encapsulation.wait_element(self, "id", "com.zsyj.wallpaper:id/tv_user_uid")
