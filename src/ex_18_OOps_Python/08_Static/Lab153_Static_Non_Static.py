class Mathoperation:
    def div (self, a, b):
        return a / b

    @staticmethod
    def sum(a, b):
        return a + b

t = Mathoperation()
print(t.div(10, 10))

print(Mathoperation.sum(10, 10))