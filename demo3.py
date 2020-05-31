"""
print("hello word")
print(123)
print(None)
print(0.3)
print(True,False)
print(())
print({})
print([])

a = "哈哈哈哈哈" #把哈哈哈赋值给a这个变量
print(a)

name = "呼呼"
print("你好,{}".format(name))


print("你好，"+name)
print("1"+"1")
print((11-3)*31+88/22)#逻辑运算符
print(10%4)#求余

print(2>1)

#input()获取输入
name = input("请输入你的姓名：")
print("这是input获取的值：",name)

#type()获取数据类型
print(type(True))

#len
print(len(123))
"""
"""
#元组() 
a = ("哈哈","123",123,True,None,123,123,123)
print(a)
print(a[0])
print(a.index(123)) #123的下标
print(a.count(123)) #元组中123的数量
print(a.count(1)) #true=1

#数组[] 元组不可以修改，数组可以修改
b = ["哈哈","123",123,True,None,123,123,123]
b.append("吴亦凡") #插在最末尾
b.insert(2,6) #插入数据到对应的位置
print(b)
c = b.pop(0) #取出
print(c)
print(b)
b.remove("123") #删除
print(b)

b.extend([1,2,3]) #添加数组
print(b)
"""
#二维数组
a = ("呼呼",1,2,3,4,5,6,None,True,"123",1,0,False)
b = ["哈哈","123",123,True,None,123,123,123]
c =[a,b]
print(c[1][1])

d = (b,0) 
print(d)
d[0].append("qiqi") #元组中的数组可以添加数据
print(d)

#字典 {}  key:value 没有顺序
x = {"name":"张张","age":22}
print(x["age"])
"""
n = x.pop("name")
print(n)
print(x)
"""
print(x.get("name"))

