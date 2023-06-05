"""
This module provides basic adder realization.Half adder and full adder are realized. 

"""
def __or_gate(a,b):
    if a == "1" or b == "1":
        output = "1"
    else:
        output = "0"
    return output



def __half_adder(a,b):
    
    if a == "1" and b == "1":
        sum = "0"
        carry = "1"
    elif a == "1" and b == "0":
        sum = "1"
        carry = "0"
    elif a == "0" and b == "1":
        sum = "1"
        carry = "0"
    elif a == "0" and b == "0":
        sum = "0"
        carry = "0"
    else:
     raise ValueError("Invalid input. Please enter either 0 or 1 for a single bit.")
    return sum, carry




def add_zeroes(a,length):   
    zero_list = ""
    for _ in range(length):
         zero_list +="0"
    return (zero_list+ a)



def __full_adder(a,b,c):

    temp_s,c1 = __half_adder(a,b)
    s,c2 = __half_adder(temp_s,c)
    c = __or_gate(c1,c2)
    return s,c




def Manage_as_byte(a):
    """Used to convert any number of character into it's Corresponding byte value. """
    if(len(a)%8==0):
        return a
    else:
        zero_to_append = 8- len(a)%8
        a= add_zeroes(a,zero_to_append)
        return a
           
        
    
def manage_length(a,b):
    """
    Used to make the length of two variables equal in length by adding leading zeros in byte form"""
    a_byte = Manage_as_byte(a)
    b_byte = Manage_as_byte(b)
    len_diff = len(a_byte) - len(b_byte)
    if(len_diff>0):
        b_changed = add_zeroes(b_byte,len_diff)
        return a_byte,b_changed
    elif(len_diff<0):
        a_changed = add_zeroes(a_byte,abs(len_diff))
        return a_changed,b_byte
    else:
        return a_byte,b_byte




def Adder(a,b):
    """Used for addition for two registers pair. Output will be a register for sum and carry flag as character"""
    print(f"A=\t{a}\nB=\t{b}\n")
    a_byte,b_byte = manage_length(a,b)
    a= a_byte[::-1]
    b = b_byte[::-1]
    sum =""
    s ,cin = __half_adder(a[0],b[0])
    sum+=s
    for i in range(1,len(a)):
        s,Cout = __full_adder(a[i],b[i],cin)
        sum+=s
        cin = Cout
    sum = sum[::-1]
    return sum,Cout



