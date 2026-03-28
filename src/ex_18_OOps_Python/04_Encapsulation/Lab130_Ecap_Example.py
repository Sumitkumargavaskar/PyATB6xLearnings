# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.

class Car:
    def __init__(self):
        self.password = "kumar"
        self.__password_secure = "pass123"

    def nany(self):
        self.__password_secure = "345"

object_ref = Car()
print(object_ref.password)
#print(object_ref.__password_secure)
object_ref.nany()
print(object_ref._Car__password_secure)