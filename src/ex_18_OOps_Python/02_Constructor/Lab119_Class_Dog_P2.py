print("Outside the class")

class Mobilephone:
    model = None

    def __init__(self):
        print("Dc")

    def talk(self):
        print("Hi,talking")

iphone = Mobilephone()
iphone.talk()
print("Outside the class2")