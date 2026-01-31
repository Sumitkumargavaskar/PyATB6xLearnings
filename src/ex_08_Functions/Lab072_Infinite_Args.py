def print_mul_args(*pramod_list):
    # args - List
    for i in pramod_list:
        print(i)

print_mul_args("pramod")
print_mul_args(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)
print_mul_args("pramod", "dutta")
print_mul_args("pramod", "dutta", "third")
print_mul_args("pramod", "dutta", "third", 3.14)
print_mul_args("pramod", "dutta", "third", 3.14, True)