#encoding=utf-8
import tkinter
import tkinter.messagebox
import webbrowser

# https://v.qq.com/x/cover/mzc00200p51jpn7/v0043tq177l.html
def Button():
    a = 'https://jx.aidouer.net/?url=' if varRadio.get() else 'https://jx.aidouer.net/?url='
    b = entry_movie_link.get()
    webbrowser.open(a+b)
def qk():
    entry_movie_link.delete(0,'end')

def openaqy():
    webbrowser.open('http://www.iqiyi.com')

def opentx():
    webbrowser.open('http://v.qq.com')

def openyq():
    webbrowser.open('http://www.youku.com/')

def openls():
    webbrowser.open('http://www.le.com/')

def openmg():
    webbrowser.open('https://www.mgtv.com/')

def opensh():
    webbrowser.open('https://tv.sohu.com/')

def about():
    abc='''
    1.可使用的链接已经提供为按钮形式
    2.链接格式为：http://www.iqiyi.com/v_19rrb2u62s.html?fc=82992814760eeac6
    =即vip所在视频网页
    '''
    tkinter.messagebox.showinfo(title='帮助文件', message=abc)
def zzxx():
    msg='''
    作者: 巳月
    声明：本软件仅供学习交流使用，请勿用于商业使用
    '''
    tkinter.messagebox.showinfo(title='联系方式', message=msg)
if __name__ == '__main__':
    root=tkinter.Tk()
    root.title('vip私人使用')
    root['width']=500
    root['height']=380

    menubar = tkinter.Menu(root)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label='帮助文档', command=about)
    helpmenu.add_command(label='作者信息', command=zzxx)
    menubar.add_cascade(label='帮助(H)', menu=helpmenu)
    root.config(menu=menubar)

    varentry1= tkinter.StringVar(value='')
    lab_movie_gallery=tkinter.Label(root, text='视频播放通道')
    lab_movie_gallery.place(x=20,y=20,width=100,height=20)
    varRadio=tkinter.IntVar(value=0)
    Radiobutton1_movie_gallery = tkinter.Radiobutton(root,variable=varRadio,value=0,text='视频通道1')
    Radiobutton2_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=1, text='视频通道2')
    Radiobutton1_movie_gallery.place(x=130,y=20,width=100,height=20)
    Radiobutton2_movie_gallery.place(x=250, y=20, width=100, height=20)

    varentry2=tkinter.StringVar(value='')
    lab_movie_link = tkinter.Label(root, text='视频播放链接')
    lab_movie_link.place(x=20, y=60, width=100, height=20)
    entry_movie_link = tkinter.Entry(root, textvariable=varentry2)
    entry_movie_link.place(x=130, y=60, width=300, height=20)
    button_movie_link=tkinter.Button(root,text='清空',command=qk)
    button_movie_link.place(x=440,y=60,width=30,height=20)
    lab_remind = tkinter.Label(root, text='将视频链接复制到框内，点击播放VIP视频')
    lab_remind.place(x=50, y=90, width=400, height=20)
    varbutton=tkinter.StringVar
    button_movie= tkinter.Button(root, text='播放VIP视频', command=Button)
    button_movie.place(x=140, y=120, width=200, height=60)

    button_movie1 = tkinter.Button(root, text='爱奇艺', command=openaqy)
    button_movie1.place(x=60, y=200, width=100, height=60)

    button_movie2 = tkinter.Button(root, text='腾讯视频', command=opentx)
    button_movie2.place(x=180, y=200, width=100, height=60)

    button_movie3 = tkinter.Button(root, text='优酷视频', command=openyq)
    button_movie3.place(x=300, y=200, width=100, height=60)

    button_movie4 = tkinter.Button(root, text='乐视视频', command=openls)
    button_movie4.place(x=60, y=280, width=100, height=60)

    button_movie5 = tkinter.Button(root, text='芒果视频', command=openmg)
    button_movie5.place(x=180, y=280, width=100, height=60)

    button_movie6 = tkinter.Button(root, text='搜狐视频', command=opensh)
    button_movie6.place(x=300, y=280, width=100, height=60)

    root.mainloop()