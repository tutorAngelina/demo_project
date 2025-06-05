def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def find_hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def print_message():
    print("This function has no input but still returns something")
    return None

def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


print(fahrenheit_to_celsius(32))
print(find_hypotenuse(0, 0))
print_message()
print(sum_list([]))