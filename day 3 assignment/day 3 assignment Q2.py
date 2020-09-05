num= input("Enter the altitude -")
num=int(num)
if num<1000:
    print("safe to land")
elif num>1000 & num<5000:
    print("bring to down 1000")
elif num>5000:
    print("turn around")
