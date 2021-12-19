
num = input("Enter a number:") #Integer number N
num = int(num)
a = 1
a1 = 2
a2 = 4

if num == 1:
    res = 1
elif num == 2: 
    res = 2
elif num == 3:
    res = 4
else:
    a3 = 0
    iplus3 = 4
    while iplus3 <= num:
        a3 = a+a1+a2
        a = a1
        a1 = a2
        a2 = a3
        iplus3 += 1
    res = a3
print(res) #final result