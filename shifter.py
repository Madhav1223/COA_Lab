def arithematic_shift_right(a):
    tmp =" "
    out_var = a[len(a)-1]
    for i in range(len(a)-1,0,-1):
         tmp+=a[i-1]
    tmp+=a[0]
    a=tmp[::-1].strip()
    return a,out_var




def arithematic_shift_left(a):
    tmp =" "
    out_var = a[0]
    for i in range(1,len(a)):
         tmp+=a[i]
    tmp+=a[-1]
    return tmp.strip(),out_var



def shift_right(a):
    tmp =" "
    for i in range(len(a)-1,0,-1):
         tmp+=a[i-1]
    tmp+='0'
    a=tmp[::-1]
    return a.strip()


