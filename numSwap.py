def swap():
    n=int(input())
    nums=list(map(int, input().split()))
    count=0
    for i in range(n-1):
        for j in range(n-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                count+=1

    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(nums[0]))
    print("Last Element: " + str(nums[n-1]))
swap()