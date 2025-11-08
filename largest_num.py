nums = input("Enter numbers: ").split()
largest = int(nums[0])
for n in nums:
    if int(n) > largest:
        largest = int(n)
print("Largest number is:", largest)
