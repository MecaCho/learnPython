import wx
'''app=wx.PySimpleApp()
app.MainLoop()
'''
app = wx.App()
win = wx.Frame(None,title="Simple Editor")
win.Show()

loadButton = wx.Button(win,label='open',pos=(200,400),size=(80,25))

saveButton = wx.Button(win,label='Save',pos=(300,400),size=(80,25))

filename = wx.TextCtrl(win,pos=(5,5),size=(80,25))

contents = wx.TextCtrl(win,pos=(5,35),size=(400,250),style=wx.TE_MULTILINE | wx.HSCROLL)

#btn = wx.Button(win)

app.MainLoop()