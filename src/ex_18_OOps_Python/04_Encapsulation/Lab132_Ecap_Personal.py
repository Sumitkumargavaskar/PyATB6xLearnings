class Home:
    def __init__(self):
        self.public_var = "Father"
        self.protected_var = "Brother"
        self.__private__var_dadsa__dasda__ = "baby"


    def mom(self):
        print(self.__private__var_dadsa__dasda__)
        self.__wife()


    def __wife(self):
        print("private wife")


object_ref = Home()
#object_ref.wife
# object_ref.__private_var
object_ref.mom()
#print(object_ref._protected_var)
# ⚠️ Technically accessible, but not recommended


