'''
What defines a function?
* Input(s)
* Output(s)

Example: f(x,y) = x + y
Inputs: x and y
Output: x + y
We call the function like f(3,4) which will compute 3 + 4 and output 7

In Python, this function would be written as...
def f(x,y):
    return x + y

And if we wanted to print the sum of 3 and 4, we would write...
print(f(3,4))

We write functions to avoid repeating ourselves. An example of this is a calculator. If you need to calculate an 
exponent like 2^6, you can manually type 2x2x2x2x2x2, or you can use the button built into the calculator.
Engineers who created the button know it is a commonly used operation and so they created a button for it.
'''

#TODO: Create a function called "squared" which computes the square of a number 
#      For example squared(4) should return 16
def squared(x):
    return x * x

number = int(input("Find the square of any number you choose in a matter of seconds!"))
print(squared(number))
