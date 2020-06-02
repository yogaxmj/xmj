#判断

#a = 123 #赋值语句，=等号左边是变量，右边是值
# b = float(input("请输入年纪："))
# if b == 18:
#     print("成年人")
#     print("后果自负")
# else:
#     print("未成年")
#     print("受保护")

#for循环
# a = [1,2,34,3,"六一儿童节"]
# for i in a: #for中in不是判断，是取值
#     print(i)

#元组
# b = ("111",1,2,1)
# for i in b:
#     print(i)

#字典
#d = {"username":"吴亦凡","age":28}
# for i in d:
#     print(i) #print的是key值
#     print(d[i]) #key值方法取值
#     print(d.get(i)) 
#     print("=========")




#判断用户是否登录

# db = [{"username":"小徐","password":"123456"},{"username":"张三","password":"12345678"}]
# zh = input("请输入账号：")
# mm = input("请输入密码：")
# #1.bug的语句
# for i in db:
#     if zh == i.get("username") and  mm == i.get("password"):
#         print("请输入账号{}登陆成功！".format(zh))
#     else:
#         print("登录失败!")


#2.
# # for i in db: #先判断账号相等
#      zh == i.get("username"): #账号相等
#         if mm == i.get("password"):
#             print("{}登录成功".format(zh))
#             break #终止循环 = 登录成功，不需要继续循环了
#     else: #账号不相等
#         continue #跳过循环，继续下一个循环


#while 
a = 1
while a < 10: #满足条件就会继续执行while里面的内容，不满足于就不会执行
    print(a)
    a = a + 1

# 1 a=1 1 a=1+1
# 2 a=2 2 a 1+2
# ....
# 8 a=8 8 a=1+8
# 9 a=9 9 a=1+9
# 10不能继续执行

#死循环 一直重复不断的运行，ctrl+C退出