def arithematic_shift_right(a):
    tmp =" "
    for i in range(len(a)-1,0,-1):
         tmp+=a[i-1]
    tmp+=a[0]
    a=tmp[::-1]
    return a




def arithematic_shift_left(a):
    tmp =" "
    for i in range(1,len(a)):
         tmp+=a[i]
    tmp+=a[-1]
    return tmp


a= input("Enter the first binary number to be shifted\t")
res = arithematic_shift_left(a)
print(res)