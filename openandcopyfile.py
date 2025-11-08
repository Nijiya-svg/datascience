f1=open("file1.txt","r")
f2=open("file2.txt","w")
w=f1.readlines()
for i in w:
    f2.writelines(i)
f2.close()
f1.close()
f2=open("file2.txt","r")
print("second file:\n ", f2.read(),sep="")
