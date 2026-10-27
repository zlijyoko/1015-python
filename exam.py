data = 10
print(type(data))

data = '十'
print(type(data))

a = print( "He is \"DOCTOR\"")

for i in range(1, 4):
    print(f"第{i:>2} 名")

x = 7
if x > 5:
    print("A")
    if x % 2 == 0:
        print("B")
    else:
        print("C")
elif x > 3:
    print("D")
print("E")

print(True or False and False)    
print((True or False) and False)  # False
print(not 3 > 5)                  

n = int(input("n="))
total = 0
for i in range(1, n + 1):
    total += i
print(f"1+...+{n}={total}")

i = 10
while i > 0:
    i -= 3
    print(i, end=" ")