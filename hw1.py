vals = [5, -1, 4, 3, 10, -192, 0, 13, 6, 17, -54]

number_of_positives = 0
number_of_negatives = 0
number_of_zero = 0
for val in vals:
    if val > 0:
        number_of_positives += 1
        print("positive")
    elif val < 0:
        number_of_negatives += 1
        print("negative")
    else:
        number_of_zero += 1
        print("zero")
print("Number of positives:", number_of_positives)
print("Number of negatives:", number_of_negatives)
print("Number of zeros:", number_of_zero)
