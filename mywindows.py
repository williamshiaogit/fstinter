# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"2131", pos = wx.DefaultPosition, size = wx.Size( 860,432 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_auinotebook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel22 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self.m_panel22, wx.ID_ANY, u"MyBotton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self.m_panel22, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self.m_panel22, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer8.Add( self.m_listBox1, 0, wx.ALL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer8.Add( self.m_filePicker2, 0, wx.ALL, 5 )


		self.m_panel22.SetSizer( bSizer8 )
		self.m_panel22.Layout()
		bSizer8.Fit( self.m_panel22 )
		self.m_auinotebook2.AddPage( self.m_panel22, u"a page", True, wx.NullBitmap )
		self.m_panel24 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 1, 1 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.m_panel24.SetSizer( bSizer9 )
		self.m_panel24.Layout()
		bSizer9.Fit( self.m_panel24 )
		self.m_auinotebook2.AddPage( self.m_panel24, u"a page", False, wx.NullBitmap )

		gSizer1.Add( self.m_auinotebook2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		gSizer1.Add( self.m_listCtrl4, 0, wx.ALL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.檔案 = wx.Menu()
		self.m_menu31 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu31.Append( self.m_menuItem4 )

		self.m_menu31.AppendSeparator()

		self.m_menuItem8 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu31.Append( self.m_menuItem8 )

		self.檔案.AppendSubMenu( self.m_menu31, u"MyMenu" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem5 )

		self.檔案.AppendSubMenu( self.m_menu4, u"MyMenu" )

		self.檔案.AppendSeparator()

		self.儲存 = wx.MenuItem( self.檔案, wx.ID_ANY, u"儲存", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.儲存 )

		self.刪除 = wx.MenuItem( self.檔案, wx.ID_ANY, u"刪除", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.刪除 )

		self.m_menubar1.Append( self.檔案, u"檔案" )

		self.編輯 = wx.Menu()
		self.測試 = wx.MenuItem( self.編輯, wx.ID_ANY, u"測試", wx.EmptyString, wx.ITEM_NORMAL )
		self.編輯.Append( self.測試 )

		self.m_menu11 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem7 )

		self.m_menuItem10 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem10 )

		self.編輯.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menubar1.Append( self.編輯, u"編輯" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.myclick1 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.myclick2 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.myclick3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def myclick1( self, event ):
		event.Skip()

	def myclick2( self, event ):
		event.Skip()

	def myclick3( self, event ):
		event.Skip()


