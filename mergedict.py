items1=input("enter the key values of 1st dictionary:").split()
items2=input("enter the key values of 2st dictionary:").split()
dict1={items1[i]:items1[i+1]for i in range(0,len(items1),2)}
dict2={items2[i]:items2[i+1]for i in range(0,len(items2),2)}
merged=dict1.copy()
merged.update(dict2)
print("merged dictionary:",merged)

