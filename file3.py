def function(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter the second number:"))

lcm = function(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}")
