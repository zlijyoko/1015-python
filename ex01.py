for i in range (5):
    print(i)

# 自代換行功能

print("**********")

for i in range (2, 6):
    print(i)

# 2, 3, 4, 5 (一行一個)

print("**********")

# for i in range(2, 6, 3):
#     print(i, end='\t')

# for i in range(2, 6, 3):
#     print(i, end=',\t,')

# t = tab (退四格)
# Start：2
# Stop：小於 6（不包含 6）
# Step：3 產生的數字序列為：2、5
#（因為下一個數字是 2 + 3 = 5，再加 3 就會大於 6，因此迴圈結束）。
# print(i, end='\t')：每次迴圈印出變數 i 的值。
# end='\t'：將預設的換行符號替換為 Tab，使輸出結果並排在同一行。

x = 0
for i in range(5):
    x+=i                   # 有這行：把算出來的新結果存回 x
    print(x, end=' ,')

x = 0
for i in range(5):
    print(x+i)
    