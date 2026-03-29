class BaseTest:
    def __init__(self, broswer):
        self.browser = broswer

    def setup(self):
        print(f"Launching {self.browser}")

class LoginTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running login test...")

class signupTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running signup test...")

t = LoginTest("chrome")
t.run_test()


t = LoginTest("Firefox")
t.run_test()

