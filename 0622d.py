import time
import os

# print("A")
# time.sleep(2)
# print("B")

# for i in range(0,10,1):
# 	os.system("cls")
# 	if i >= 0 and i <= 3:
# 		print("您好",i)
# 		time.sleep(0.5)
# 		os.system("cls")
# 	elif i >= 4 and i<= 7:
# 		print("哈囉",i)
# 	else:
# 		print("哈哈",i)
# 	time.sleep(1)

# print(time.time())
# time.sleep(0.001)
# print(time.time())


# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%X %x"))

# pip list 可以列出目前安裝的函式庫
# pip install 函式庫名稱

import prettytable

# t=prettytable.PrettyTable(["ID", "Title","帥嗎"], encoding="utf8")
# t.align["Title"]="r" #"l"靠左 "c"至中 "r"靠右
# t.add_row([1, "aaa","不"])
# t.add_row([2, "bbb","帥"])
# t.add_row([3, "ccccccccc","不"])
# print(t)
# t.align["Title"]="l"
# print(t)

import colorama
#初始化設定 自動清除
colorama.init(True)

# print(colorama.Style.BRIGHT+"abcABC")
# print(colorama.Fore.RED+colorama.Style.BRIGHT+"abcABC")
# print(colorama.Fore.RED+"abcABC")
# print(colorama.Fore.MAGENTA+"abcABC")
# print(colorama.Fore.CYAN+"abcABC")
# print(colorama.Fore.BLUE+"abcABC")
# print(colorama.Back.RED+"abcABC")

# print(colorama.Back.RED+colorama.Fore.RED+"abc")
# a=0
# while a == 0:
# 	for i in range(0,10,1):
# 		os.system("cls")
# 		i+=1
# 		if i-1 >= 0 and i-1 <= 4:
# 			print(colorama.Back.RED+colorama.Fore.RED+"abc")
# 			print(i)
# 			# time.sleep()
# 		elif i-1 >= 5 and i-1 <= 5:
# 			print("  ",colorama.Back.YELLOW+colorama.Fore.YELLOW+"abc")
# 			print(i)
# 		else:
# 			print("     ",colorama.Back.GREEN+colorama.Fore.GREEN+"abc")
# 			print(i)
# 		time.sleep(1)

#pip install wxPython

import mywindows
import wx
import codecs

class myframe1(mywindows.MyFrame1):
	def myclick(self,event):
		self.SetTitle("標題文字")
		wx.MessageBox("abc")

	def myclick1( self, event ):
		self.SetTitle("標題文字")
		wx.MessageBox("abc")

	def myclick2( self, event ):
		r=self.m_filePicker2.GetPath()
		wx.MessageBox(r)
		with codecs.open(r,"r","utf8") as f:
			self.m_listCtrl4.SetValue(f.read())

	def myclick3( self, event ):
		event.Skip()




# a=wx.App()
# w=myframe1(None)

# w.Show()
# a.MainLoop()

app=wx.App()
win=myframe1(None)
win.Show()
app.MainLoop()

