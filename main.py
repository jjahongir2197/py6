def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

sorted_numbers = bubble_sort(numbers)

print("Sorted:", sorted_numbers)
