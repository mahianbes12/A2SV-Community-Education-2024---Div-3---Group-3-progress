def countingSort(arr):
    max_value = max(arr)
    frequency = [0] * (max_value + 1)

    for num in arr:
        frequency[num] += 1

    sorted_array = []
    for num, count in enumerate(frequency):
        sorted_array.extend([num] * count)

    return sorted_array

n = int(input())
arr = list(map(int, input().split()))

result = countingSort(arr)
print(*result)
