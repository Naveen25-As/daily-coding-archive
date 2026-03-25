# Compund interest

p = float(input("Enter principle:"))
r = float(input("Enter rate:"))
t = float(input("Enter time:"))
ci = p * ( 1 + r/100 ) ** t - p
print("Compund interest:",ci)