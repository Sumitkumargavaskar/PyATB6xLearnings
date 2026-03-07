class person:
    #Attributes
    name = None
    id =  None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    #Behaviour
    def talk(self):  # self - this , self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self, name): # Arg with No Return
        print("I am a method!!")
        print("sleep", name)


    def sleep2(self, name): # Arg with Return
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def method_walk_return(self):  # No Arg with Return
        return "I am walking"



    def function_outside():
        print("I am outside")


# Create an Object of the Class
# ObjectRef = ClassName() -> Object
geeta = person()
amit =  person()
navita = person()

print(geeta.name)
geeta.sleep("pramod")

