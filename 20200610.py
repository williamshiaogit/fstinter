a=10
b="10ahbobebbbibgbb"
c=[]
d=()


# print(c,"xxx")
# print(a/3)
# x=a*5
# print(x)
# a+=10
# print(a)
# q="50"
# print(b+q,end="")#end預設\n 設為空白就不會換行
# print("abc\nde\nf\ng")
# print(b.replace("b","*"))
# print(b.count('a\"*"'))

# print(b[0])
# print(b[0:-1])
# cc=[1,2,3,4,5]
# cc[2]='A'
# print(cc[2])
# q=cc[2:5]
# print(cc)
# print(len(cc))
# print(len(q))
# print(cc+q)
# print(q+cc)
# print(cc*3)
# print(cc.index('A'))
# print((cc*5).count(4))

e={
	"a":10,
	"b":20,
	"c":30
}
# print(e)
# print(e["b"])
# e["b"]="A"
# print(e["b"])
# print(e)

# x=list(e.keys()) #字典變成列表
# print(x)
# print(x[0])
# y=list(e.values())
# print(y)
# print(y[0])
# e["d"]=40 #增加
# print(e)

#函式
# def xxx():
# 	print("A") #空白跟Tab 不要交換用
# 	print("B") #縮排在裡面 代表 在函式裡面
# 	return "abcde"
# print("C")
# xxx()
# print(xxx())

def yyy(a=5,b=10): #可選參數給初始值=
	global c
	c=a+b
	return c*3, "abcdefg" #回傳很多值 用逗號
x,y=yyy(4,5) #return幾個值用幾個變數
print(yyy(a=7)) #可以指定要給a或b(要定義上面有給初始值)
print(c)
print(x)
print(y)
