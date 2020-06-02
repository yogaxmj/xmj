for b in range(3,0,-1):
    print("黄灯还有",b,"秒结束")
for b in range(35,0,-1):
    print("绿灯还有",b,"秒结束")
for b in range(30,0,-1):
    print("红灯还有",b,"秒结束")   

  


username = input("账号")
password = input("密码")
if len(username) >=3 and len(username) <= 8:
    print("username")
    if username[0] in "zxcvbnmlkjhgfdsaqwertyuiop":
        print("username")
        if len(password) >=6 and len(password) <=8:
            print("注册成功",{username,password})
        else:
            print("密码必须为6-8位")
    else:
        print("账号开头必须为小写")
else:
    print("账号必须位3-8位")