
#print("請輸入:", end="")
#r=input("")


# r=input("輸入:")
# #print("你輸入了",r)

# if r.find("a")!=-1:
# 	print("你好")
# elif r.find("b")=1:
# 	print("哈囉")
# else:
# 	print("哈哈哈")

# x="1,2,3,4,5,6,7"
# z=x.split(",")#切割 split("做為切割的字串")
# print(z)
# for i in z:
# 	print(i)

# x=input("請輸入生日:")#切割範例
# z=x.split("-")
# print(z[0], "年")
# print(z[1], "月")
# print(z[2], "日")

# x=["A","B","C"] #串列合起來成字串
# z="".join(x)
# print(z)

# #範例
# x = [input("國家:"),input("城市:"),input("地址:"),input("號碼")]
# z = "".join(x)
# print(z)

#載入模組
# import sys
# print(sys.argv)

import os
# os.system("dir")
# os.system("tasklist")

# p=os.popen("tasklist")
# x=p.read()
# #print(x)

# y=False
# for a in x:
# 	if a.find("notepad.exe")!=-1:
# 		y=True

# if y==True:
# 	print("記事本已開啟")
# else:
# 	os.system("notepad.exe")

# p=os.popen("tasklist")
# x=p.read()

# import webbrowser
# u=input("請輸入網址:")
# webbrowser.open(u, new=1, autoraise=True)
# import os
# import sys
# ff=sys.argv[1]
# 


# os.system('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" ')
# y=False
# for a in x:
# 	if a.find("notepad.exe")!=-1:
# 		y=True

# if y==True:
# 	print("記事本已開啟")
# else:
# 	os.system("notepad.exe")

import codecs
# f=codecs.open("1.txt", "r", "utf8") #w寫入 r讀取 a附加 b二進位
# # f.write("abc")
# x=f.read()
# f.close()
# print(x)

#b二進位 複製圖片
# f=codecs.open("1.png", "rb")
# # f.write("abc")
# x=f.read()
# f.close()
# # print(x)

# f=codecs.open("2.png", "wb")
# f.write(x)
# f.close()

#with讓檔案在範圍內(自動關閉)
# with codecs.open("1.txt", "r", "utf8") as f:
# 	x=f.read()
# with codecs.open("2.txt", "w", "utf8") as f:
# 	f.write(x)

# os.remove("2.png")
# os.mkdir("xxx")
# os.rmdir("xxx")

# r=os.listdir("D:/")#取出變成list
# rr=os.listdir("./")#./代表當前資料夾
# rrr=os.listdir("../")#../代表當前資料夾的上一個資料夾
# print(r)
# print(rr)
# print(rrr)

# for d in rr:
# 	print(d)
# 	pp=d.find("0620.py")
# 	print(pp)

# print("工作路徑:", os.getcwd())#取得當前工作路徑
# print(os.listdir("./"))
# os.chdir("../")
# print("工作路徑:", os.getcwd())
# print(os.listdir("./"))

# print(os.path.isdir("../python"))
# print(os.path.isdir("1.txt"))
# print(os.path.exists("1.txt"))
# print(os.path.isfile("1.txt"))

# print(os.path.basename("./0620.py"))
# priny(os.path.getsize("./0620.py"))

# def read_dir(r,t):
# 	z= os.listdir(r)
# 	for d in z :
# 		if os.path.isdir(r+"/"+d)==True:
# 			read_dir(r+"/"+d,t)
# 		if d.find(t)!=-1:#if t in d:
# 			print(r+"/"+d)
# read_dir("D:/python", "0")


x=""
while x!=0:
	os.system("cls")
	
	fileList=[]
	dirList=[]
	for d in os.listdir("./"):
		if os.path.isdir(d)!= True:
			fileList+=[d]
		else:
			dirList+=[d]

	if x=="1":
		for i in range(0,len(fileList),1):
			print(i, fileList[i])
		print("")
		# y=os.listdir("./")
		# y="\n".join(y)
		# print(y)
	elif x=="2":
		for i in range(0, len(dirList), 1):
			print(i,dirList[i])
		print("")
		# ff = os.listdir("./")
		# for fe in ff:
		# 	e = os.path.isdir(fe)
		# 	if e==True:
		# 		print(fe)
	elif x=="3":
		for i in range(0,len(fileList),1):
			print(i, fileList[i])
		print("")
		p=input("請輸入檔案索引:")
		os.system("cls")
		print("=====檔案開始=====")
		with codecs.open(fileList[int(p)], "r", "utf8") as f:
			print(f.read())
		print("=====檔案結束=====")
		print("")
		# os.system("cls")
		# y=os.listdir("./")
		# y="\n".join(y)
		# print(y)
		# input("請輸入檔案索引:")
		# f=codecs.open(fi, "r", "utf8") 
		# x=f.read()
		# f.close()
		# print(x)
	elif x=="4":
		for i in range(0,len(fileList),1):
			print(i, fileList[i])
		print("")
		pd=input("請輸入要刪除的檔案索引:")
		os.system("cls")
		os.remove(fileList[int(pd)])
		print("")
	elif x=="5":
		for i in range(0,len(fileList),1):
			print(i, fileList[i])
		print("")
		pp=input("請輸入要執行的檔案索引:")
		os.system("cls")
		os.popen(fileList[int(pp)])
	elif x=="6":
		for i in range(0, len(dirList), 1):
			print(i,dirList[i])
		print("")
		dd=input("請輸入資料夾索引：")
		os.chdir(dirList[int(dd)])
		print("")
	elif x=="7":
		for i in range(0, len(dirList), 1):
			print(i,dirList[i])
		print("")
		rd=input("請輸入資料夾索引：")

		# os.rmdir(dirList[int(rd)])
		def rm_dir(r):
			
			for d in dirList:
				if os.path.isdir(r+"/"+d)==True:
					rm_dir(r+"/"+d)
				else:
					os.remove(r)
				# if d.find()!=-1:
				# 	rmdir("./")
		rm_dir(dirList[int(rd)])
	elif x=="8":
		os.chdir("../")




	print("工作路徑:", os.getcwd())
	print("(0) 離開程式")
	print("(1) 列出檔案")
	print("(2) 列出資料夾")
	print("(3) 顯示檔案內容")
	print("(4) 刪除檔案")
	print("(5) 執行檔案")
	print("(6) 進入資料夾")
	print("(7) 刪除資料夾")
	print("(8) 回上層資料夾")
	x = input("操作:")


