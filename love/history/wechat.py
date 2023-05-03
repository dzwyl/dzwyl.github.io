from wxauto import *

send_msg='sorry'
who='玲宝'
wx=WeChat()

for i in range(5):
    wx.ChatWith(who)
    wx.SendMsg(send_msg)
    i=i+1
