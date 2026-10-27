
# i, total = 1, 0
# while i <= 10:
#     total += i
#     i += 1
# print(total)


n = 7
for d in range(2, n):
    if n % d == 0:
        print(n, "不是質數")
        break
else:
    print(n, "是質數")  


n = [3, 8, 12, 5]
for x in n:
    if x > 10:
        print(x)
        break
else:
    print("沒有大於 10 的數")

scores = [72, 58, 91, 45, 100]
total, count, found = 0, 0, False

for s in scores:
    total += s          # 累加總分
    
    if s >= 60:         # 縮排進來：檢查每一個分數是否及格
        count += 1      
        
    if s == 100:        # 縮排進來：檢查每一個分數是否為 100
        found = True

print(total, count, found)  # 執行結果會是：366 3 True