# x=-1

# if x > 0:
# 	print("A")
# elif x<0:
# 	print("B")
# else:
# 	print("C")

# x=[1,2,"3",4,5]

# if 3 not in x:
# 	print("A")
# else:
# 	print("B")

# x={
# 	"a":100,
# 	"b":200,
# 	"c":300
# }
# if x["a"] in x :
# 	print("A")
# else:
# 	print("B")

# y=list(x.values())
# print(y)
# if 200 in y:
# 	print("A")
# else:
# 	print("B")

# if "a" in x:
# 	print("A")
# elif"b" in x:
# 	print("B")
# elif "E" in x :
# 	print("E")

# a=000000000000000
# for x in range(0,11,6):
# 	a+=x
# 	print("x=",x)
# print("總共",a)

# a=0
# x=0
# while x<1000000:
# 	x+=1
# 	a+=x
# print(a)

# a=0
# x=0
# while x<1000000:
# 	x+=1
# 	a+=x
# 	if x >= 10:
# 		break
# print(a)


# a=0
# x=0
# while x<1000000:
# 	x+=1
	
# 	if x == 500:
# 		continue
# 	a+=x
# print(a)

# x=0
# def test(a,b):
# 	try :
# 		x=a*2+b**2 #try:程式碼出錯後才執行except: 最後執行finally:
# 	except:
# 		x="型態錯誤了笨蛋!"
# 	finally:
# 		print("你好",end=" ")
# 		return x
# test(10,5)
# print(test(10,5))
# print(test(10,"9"))

#作業一 九九乘法表
# a=0
# p=0
# for a in [1,2,3,4,5,6,7,8,9]:
# 	for p in [1,2,3,4,5,6,7,8,9]:
# 		c=a*p 
# 		print(a,"x",p,"=",c,end="  ")
# 	print(" ")

#類別!!
class aa:
	x=100
	def test(self,a):
		return 200+self.x
	def __init__(self,a):
		print("init")

	@staticmethod #直接使用? 靜態方法
	def test2():
		return 201
	@classmethod #指向類別本身? 類別方法
	def test3(cls):
		return 400
			
print("===直接用類別名稱呼叫===")
#print(aa.test(100)) 會出錯
print(aa.test2())
print(aa.test3())

# class bb:
# 	x="ABC"
# 	def test(self):
# 		return "XXX"+self.x
# 	def __init__(self):
# 		print("INIT")

print("===使用類別變數w1呼叫===")
w1=aa(111)
print(w1.test(100))
print(w1.test2())
print(w1.test3())
print(w1.x)


# w2=bb()
# print(w2.x)
# print(w2.test())

# print(aa.test2())
# print(aa.test3())

class cc:
	x=100
	def test(self,a):
		return 200+self.x
	def __init__(self,a):
		print("init",self,a)

print(cc(10))