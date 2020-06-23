
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
# sys.argv[1]


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
f=codecs.open("1.txt", "r", "utf8") #w寫入 r讀取 a附加 b二進位
# f.write("abc")
x=f.read()
f.close()
print(x)

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
with codecs.open("1.txt", "r", "utf8") as f:
	x=f.read()
with codecs.open("2.txt", "w", "utf8") as f:
	f.write(x)
