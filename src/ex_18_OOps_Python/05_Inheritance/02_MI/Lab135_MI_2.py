class Father1:
    def money(self):
        print("F1 Money")

class Father2:
    def money(self):
        print("F2 Money")

class child(Father1, Father2):
    def give_money(self):
        print("son")
        self.money()

c = child()
c.give_money()