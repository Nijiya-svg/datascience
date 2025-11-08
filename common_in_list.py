list1 = input("Enter first list of elements separated by spaces: ").split()
list2 = input("Enter second list of elements separated by spaces: ").split()

common = any(item in list2 for item in list1)

print(common)
