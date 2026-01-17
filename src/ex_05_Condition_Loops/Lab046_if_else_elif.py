# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1 = int(input("Enter a num1\n: "))     # 5 , # 10
num2 = int(input("Enter the num2\n: "))    # 3 , # 12
num3 = int(input("Enter the num3\n: "))     # 2 , # 11

# 5 > 3 and 5 >2 ->  5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 nad num2 > num3 -> num2
# num3 - max

if num1 >= num2 and num1 >= num3:
    print("Maximum", num1)
elif num2 >= num3 and num2 >= num1:
    print("Maximum", num2)
else:
    print("Maximum", num3)