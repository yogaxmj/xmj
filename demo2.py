high = {}
low = {}
a = {"aa","dd","cc","dd"}
for i in a:
    score = int(input("请输入"+i+"成绩："))
    if score >= 60:
        high[i] = score
    else:
        low[i] = score
print("大于60",high)
print("小于60",low)
         