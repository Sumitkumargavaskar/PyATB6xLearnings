class BaseTest:
    def setup(self):
        print("Setup from BaseTest")

class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")


class signupTest(BaseTest):
    def run(self):
        print("Running Signup Test")

LoginTest().setup()
LoginTest().run()
signupTest().setup()
signupTest().run()