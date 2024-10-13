import time


class TestLogin:

    def test_login(self,setup_and_teardown):
        self.homepage.signIn_btn()
        time.sleep(5)
        self.loginpage.login('prasadhatwar','prasadhatwar01@12')
    
            