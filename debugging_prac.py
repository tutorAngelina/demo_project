def count_large(numbers):
    count = 0
    for num in numbers:
        if num > 10:
            count += 1
    return count

nums = [5, 10, 12, 7, 10, 15]
print("Count:", count_large(nums))
