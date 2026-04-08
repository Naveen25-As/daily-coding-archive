# Atomorphic numbers under 1000

print("Automorphic numbers between 1 to 1000 : ")

for num in range(1,1001):
    square = num * num
    
    if str(square).endswith(str(num)):
        print(num)