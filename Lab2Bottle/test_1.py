import unittest
import myform_mail as mm
class Test_test_1(unittest.TestCase):
    def test_A(self):
        list_mail_cor = ["m.m@mail.ru", "m1@gmail.com", "pradauhufruffo-3111@yopmail.com", 
                         "rizupequeule-8209@yopmail.com", "kobayasi@mac.com", "jonas@gmail.com", 
                         "jmorris@comcast.net","horrocks@att.net", "nicola_halvorson@hotmail.com", 
                         "stephon28@yahoo.com", "eduqsnk535@fatamail.com", "tinytmp-qo1vp@gmail.com"]
        for x in list_mail_cor:
            self.assertTrue(mm.mail_match(x))
    def test_B(self):
        list_mail_incor = ["", "1", "m1@", "@mail", 
                           "@mail.com", "ttt@tuyi", "jdsod@2jj.t", "1@11.11", 
                           "d^*$%@cn.com", "kseniia@.com", "kseniia@icloud.com1", "jfkj@^^fn2.com"]
        for x in list_mail_incor:
            self.assertFalse(mm.mail_match(x))

if __name__ == '__main__':
    unittest.main()
