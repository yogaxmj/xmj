#用户信息
db = [{"username":"chenke","password":"123456"}]

#输入账号密码
zh = input("请输入账号：")
mm = input("请输入密码：")

#循环db并且判断是否存在重复账号，如果重复--改密码，否则--新增账号

for i in db:
    if zh == i.get("username"):
        i["password"] = mm
        break
    else:
        db.append({"username":zh,"password":mm})
        # c = {}
        # c["username"] = zh
        # c["password"] = mm
        # db.append(c)
print(db)
