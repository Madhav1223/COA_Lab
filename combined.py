import circuit
def manage_c(c,i):
    temp =""
    for _ in range(i):
        temp+=c
    return temp   

def both(a,b,c):
    b_byte,c_byte = circuit.manage_length(b,c)
    c_byte=manage_c(c,len(b_byte))
    print(f"C is\t{c_byte}\nB is\t{b_byte}")
    temp_sum = circuit.Adder(b_byte,c_byte)[0]
    print(f"Generated first Sum = \t{temp_sum}\n")
    
    a_byte,temp_sum = circuit.manage_length(a,temp_sum)
    temp_sum = temp_sum[::-1]
    a_byte = a_byte[::-1]
    s,cin = circuit.full_adder(a_byte[0],temp_sum[0],c)
   
    sum=s
    for i in range (1,len(a_byte)):
       s_out,cout= circuit.full_adder(a_byte[i],temp_sum[i],cin)
       sum+=s_out
       cin = cout

    print(f"Sum =\t{sum[::-1]}\nCarry=\t{cout}")


a= input("Enter the first binary number to be added:\t")
b= input("Enter the Second binary number to be added:\t")
c=input("Enter 0 for addition and 1 for subtraction:\t")
print(f"A=\t{a}\nB=\t{b}\nC=\t{c}")
both(a,b,c)