import circuit
import shifter
import signed_circuit


def partial_prod(a,b):
    a = circuit.Manage_as_byte(a)
    b = circuit.Manage_as_byte(b)
    acc, a = circuit.manage_length('0', a)
    for _ in range(len(b)):
        print(f"Acc = {acc}\nB = {b}\nLast bit = {b[-1]}")
        if b[-1] == '0':
            tmp = acc + b
            tmp = shifter.shift_right(tmp)  
        elif b[-1] == '1':
            sum_result = circuit.Adder(acc, a)[0]  
            print(f"Sum is: {sum_result}\n")
            tmp = sum_result + b
            tmp = shifter.shift_right(tmp)
        else:
            raise ValueError("Not a binary representation")
        acc = str(tmp[:len(a)]).strip()
        b = str(tmp[len(a):]).strip()
        print()
    return tmp


def booth_multiplier(a,b):
    a = signed_circuit.Manage_as_signed_byte(a)
    b = signed_circuit.Manage_as_signed_byte(b)
    acc, a = circuit.manage_length('0', a)
    print(f"a={a}\nb={b}\nacc={acc}\n")
    b_img ='0' 
    tmp = acc + b
    for _ in range(len(b)):
        if (b_img =='0' and b[-1]=='1'):
            sum_tmp = circuit.Subtractor(acc,a)[0]
            tmp = sum_tmp+b
        
        elif (b_img =='1' and b[-1]=='0'):
                sum_tmp = circuit.Adder(acc,a)[0]
                tmp = sum_tmp+b
        tmp,b_img = shifter.arithematic_shift_right(tmp)
        acc = str(tmp[:len(a)]).strip()
        b = str(tmp[len(a):]).strip()
        print(f"{acc} {b}")

    return tmp

                


a = input("Enter the Multiplicand:\t")
b = input("Enter the Multiplier:\t")
#result = partial_prod(a,b)
result = booth_multiplier(a,b)
print(f"The result of the multiplication is: {result}")





