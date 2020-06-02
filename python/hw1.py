db = [{"username":"chenke","password":"123456"}]

zh = input("请输入账号：")
mm = input("请输入密码：")

count = 1
for i in db:
    if zh == i.get("username"):
        i["password"] == mm
        break
    else:
        if len(db) == count:
            db.append({"username":zh,"password":mm})
        count = count + 1

print(db)
