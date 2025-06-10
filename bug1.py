''' 
This code should print out the average of only the even numbers in a list.
It does not always work as intended.
Remember: % represents the modulus operator. It returns the remainder of a division problem.
      Ex:  13 % 3 = 1 since 13/3 = 4 remainder 1
1. Put a breakpoint on line 13 to help find the bug
2. For which values in the list result in the if-statement returning true?
3. How can we fix this?
'''
def average_of_evens(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
            count += 1
    return total / count

nums = [4, 9, 6, 7, 8]
print("Average of even numbers:", average_of_evens(nums))