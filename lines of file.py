filename=input("enter the filename:")
with open(filename,"r")as f:
    line_count=sum(1 for line in f)
    print("number of lines:",line_count)

