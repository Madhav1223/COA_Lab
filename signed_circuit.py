import circuit



def add_ones(a,length):   
    ones_list = ""
    for _ in range(length):
         ones_list +="1"
    return (ones_list+ a)


def Manage_as_signed_byte(a):
    """Used to convert any number of character into it's Corresponding byte value. """
    if(len(a)%8==0):
        return a
    else:
        if(a[0]=='0'):
            zero_to_append = 8- len(a)%8
            a= circuit.add_zeroes(a,zero_to_append)
        else:
            ones_to_append = 8- len(a)%8
            a= add_ones(a,ones_to_append)
        return a
    
'''
def manage_signed_length(a,b):
    a_byte = manage_signed_length(a)
    b_byte = manage_signed_length(b)
    if (len(a)>len(b)):
        if(b[0]=='0'):
            circuit.add_zeroes(b,len(a)-len(b))
        else:
            add_ones(b,len(a)-len(b))
    
'''
