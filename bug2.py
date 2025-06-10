'''
Find the bug.
Hint #1: Sum up the total up to 5 by hand. What values do you have to add together?
Hint #2: Put a breakpoint on line 12.
      What is the last value of i that gets added to the total?
      Is this the i-value you expected?
'''

def sum_up_to(n):
    total = 0
    for i in range(1, n):
        total += i
    return total

print("Sum up to 5:", sum_up_to(5))   # Should be 15
print("Sum up to 10:", sum_up_to(10)) # Should be 55
