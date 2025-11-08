pairs=input("enter the key value pairs seperated by space:").split()
t=[(pairs[i],pairs[i+1])for i in range(0,len(pairs),2)]
d=dict(t)
print("dictionery:",d)
