from time import sleep
import unittest
import sys
import time
from part_04.test_case.models import myunit
from part_04.test_case.models import function

from part_04.test_case.page_obj.loginPage import login

sys.path.append('./models')
sys.path.append('./page_obj')

class loginTest(myunit.MyTest):

    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        self.user_login_verify(username='username', password='password')
        po = login(self.driver)
        self.assertEqual(po.user_login_sucess(),'检测系统')
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        img_name = now_time + '.png'
        function.insert_img(self.driver, img_name)

    if __name__ == '__main__':
        unittest.main()

