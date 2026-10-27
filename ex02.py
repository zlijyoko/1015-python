# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

a,b,c = map(int, input('請輸入 a b c : ').split())

if 0 < a < c < b:
    for i in range(a, b+1):
        i * c
        if a < i*c <= b:
            print(i*c)
else:
    print('輸入錯誤')


a,b,c = map(int, input('請輸入 a b c : ').split())

if 0 < a < c < b:
    for i in range(a, b+1):
        if i%c == 0 :
            continue
else:
    print()