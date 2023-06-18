import circuit


a= input("Enter the first binary number to be added:\t")
b= input("Enter the Second binary number to be added:\t")
s,c = circuit.Subtractor(a,b)
print(f"Sum=\t{s}\nBorrow =\t{c}")

