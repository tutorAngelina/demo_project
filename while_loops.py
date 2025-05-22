'''
In this file, we will learn a little bit about receiving the user's input with a while loop.

To receive user input, we use:
input()
Typically we like to keep track of this input by assigning it to a variable, otherwise the last line does nothing.
user_input = input()

If we want to give the user a prompt, we can add a string to the input() function like this:
user_input = input("Enter your name: ")
The user will see:
Enter your name: 

While loop format:
while(condition):
    do something

For reading user input, we can use the following conditions in the while loop:
* user_input - reads user_input forever
* user_input != "stop condition" - reads user input until they enter some stop trigger like 'quit' or 'exit'
'''