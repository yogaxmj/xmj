import time
now = time.strftime("%y-%m-%d %H:%M:%M")
text = input("输入")
with open("D:\日记.text","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-------------\n" )
#文件写入


