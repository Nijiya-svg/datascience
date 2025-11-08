from datetime import datetime

date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

if date1 < date2:
    print(f"{date1_str} is earlier than {date2_str}")
elif date2 < date1:
    print(f"{date2_str} is earlier than {date1_str}")
else:
    print("Both dates are the same.")
