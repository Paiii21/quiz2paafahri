import random

random_numbers = [random.randint(0, 100) for _ in range(50)]

sorted_numbers = sorted(random_numbers)

print("Original Numbers:", random_numbers)
print("Sorted Numbers (Naive):", sorted_numbers)

with open("naive_output.txt", "w") as file:
    file.write("Original Numbers:\n")
    file.write(str(random_numbers) + "\n")
    file.write("Sorted Numbers (Naive):\n")
    file.write(str(sorted_numbers) + "\n")