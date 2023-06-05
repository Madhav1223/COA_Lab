from circuit import Adder


a= input("Enter the first binary number to be added:\t")
b= input("Enter the Second binary number to be added:\t")
sum,carry =Adder(a,b)
print(f"Sum =\t{sum}\nCarry =\t{carry}")
