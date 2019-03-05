from basedata.two_encapsulation import Two_Encapsulation
from basedata.base_test_case import BaseTestCase


class Xm_sp(Two_Encapsulation):

    def xtest_wx_login(self):
        Two_Encapsulation.element_click(self, 'id', '')

