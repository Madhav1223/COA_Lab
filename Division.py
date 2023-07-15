import circuit
import signed_circuit
import shifter
def restore(dividend,divisor,acc):
    temp_list = list(acc+ dividend)
    temp = acc+ dividend
    print(f"{acc}\t{dividend}")
    for _ in range(len(dividend)):
        print(f"{temp}\n")
        temp = shifter.arithematic_shift_left(temp)[0]
        acc = temp[:len(dividend)]
        acc = circuit.Subtractor(acc,divisor)[0]
        temp_list = list(temp)
        if(acc[0]=='1'):
            acc = circuit.Adder(acc,divisor)[0]
            temp_list[:len(dividend)] = acc.strip()
            temp_list[-1]='0'
        else:
            temp_list[:len(dividend)] = acc 
            temp_list[-1]='1'
        temp = ''.join(temp_list)

    print(f"Quotient=\t{temp[len(dividend):]}\nReminder=\t{temp[:len(dividend)]}")
    return


def non_restore(dividend,divisor,acc):
    temp_list = list(acc+ dividend)
    temp = acc+ dividend
    Subtract = True
    print(f"{acc}\t{dividend}")
    for _ in range(len(dividend)):
        print(f"{temp}\n")
        temp = shifter.arithematic_shift_left(temp)[0]
        temp_list = list(temp)
        acc = temp[:len(dividend)]
        if(Subtract):
            acc = circuit.Subtractor(acc,divisor)[0]
        else:
            acc = circuit.Adder(acc,divisor)[0]
       
        temp_list[:len(dividend)] = acc 
        if(acc[0]=='1'):
            Subtract = False
            temp_list[-1]='0'
        else:
            
            temp_list[-1]='1'
            Subtract = True
        temp = ''.join(temp_list)

    if(not Subtract):
        acc = circuit.Adder(acc,divisor)[0]
        temp_list[:len(dividend)] = acc 
        temp = ''.join(temp_list)

    print(f"Quotient=\t{temp[len(dividend):]}\nReminder=\t{temp[:len(dividend)]}")
    return



# dividend = input("Enter the dividend:\t")
dividend = '1111'
# divisor = input("Enter the Divisor:\t")
divisor = '111'
dividend_byte = circuit.Manage_as_byte(dividend)
divisor_byte = circuit.Manage_as_byte(divisor)
acc,divisor_byte= circuit.manage_length('0',divisor_byte)
# restore(dividend_byte,divisor_byte,acc)
non_restore(dividend_byte,divisor_byte,acc)
