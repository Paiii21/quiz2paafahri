import random

random_numbers = [random.randint(0, 100) for _ in range(50)]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sorted_numbers = random_numbers.copy()
merge_sort(merge_sorted_numbers)

print("Original Numbers:", random_numbers)
print("Sorted Numbers (Merge Sort):", merge_sorted_numbers)

with open("conquer_output.txt", "w") as file:
    file.write("Original Numbers:\n")
    file.write(str(random_numbers) + "\n")
    file.write("Sorted Numbers (Merge Sort):\n")
    file.write(str(merge_sorted_numbers) + "\n")
