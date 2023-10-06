import random
import tkinter
from tkinter import *

import S_des
from PIL import ImageTk, Image

def get_info():
    p = entry1.get()
    K = entry2.get()
    a = S_des.end(p, K)
    b = S_des.over(a,K)
    print(a,b)
    show(a)

def ascii_to_char(ascii_code):
    return format(ascii_code, 'c')

def char_to_ascii(char):
    return ord(char)

def rand():
    x = ""
    for i in range(10):
        a = str(random.choice([0,1]))
        x = x + a
    return x

def show(a):
    print(a)
    win1 = tkinter.Tk()
    win1.title("加密结果！")
    win1.geometry("350x250+573+300")
    label = tkinter.Label(win1, fg="#001c3d", text=a)
    label.pack()
    label.config(font=('楷体', 15), fg='#001c3d')
    label.place(x=142, y=100)
    # e = tkinter.Entry(win1,background="#f1e9ff")
    # e.insert(END,a)
    # e.pack()
    # e.config(font=(15), fg='#001c3d')
    # e.place(x=142, y=180)




def show_2():
    win = tkinter.Tk() #构造窗体
    win.title("S-DES(二进制)")#标题
    '''
    400x200+400+300
    分别对应: 
    400宽度
    200高度
    300(x坐标,即横坐标,作用是设置出现的程序界面位于屏幕的哪个位置[左或者右])
    310(y坐标,即纵坐标,作用是设置出现的程序界面位于屏幕的哪个位置[上或者下])
    '''
    win.geometry("400x250+550+300")  #设置窗口的大小,具体方法在上面的注释已说明

    label1 = tkinter.Label(win,fg="#001c3d",text="加密内容: ")
    label1.pack()
    label1.config( font=('楷体',15),fg='#001c3d')
    label1.place(x=45, y=40)

    global entry1
    entry1 = tkinter.Entry(win,width=20,font=15,highlightcolor="#d4e2fc")
    entry1.pack()
    entry1.place(x=145, y=42)

    label2 = tkinter.Label(win,text="密钥: ")
    label2.pack()
    label2.config( font=('楷体',15),fg='#001c3d')
    label2.place(x=85, y=80)

    global entry2
    entry2=tkinter.Entry(win,width=20,font=3)
    entry2.pack()
    entry2.place(x=145, y=82)

    button1 = tkinter.Button(win, text="确定", width=10, height=1,background="#dcd0ff",command=get_info)
    button1.pack()   #加载到窗体
    button1.place(x=160, y=180)  #设置坐标（以程序界面大小为基准)

def get_info_en():
    p = entry3.get()         #            英文内容
    K = entry4.get()         #            密钥
    print(p,K)
    q = ""
    for x in p:
        a = S_des.to_10_2_8(char_to_ascii(x))
        print("H",a)
        ab = S_des.end(a, K)
        print("H", ab)
        b = S_des.to_2_10(ab)
        print("H", b)
        y = ascii_to_char(b)
        print("H", y)
        q = q + y
        print("H", q)
    show(q)


def show_3():
    win = tkinter.Tk() #构造窗体
    win.title("S-DES(英文)")#标题
    '''
    400x200+400+300
    分别对应: 
    400宽度
    200高度
    300(x坐标,即横坐标,作用是设置出现的程序界面位于屏幕的哪个位置[左或者右])
    310(y坐标,即纵坐标,作用是设置出现的程序界面位于屏幕的哪个位置[上或者下])
    '''
    win.geometry("400x250+550+300")  #设置窗口的大小,具体方法在上面的注释已说明

    label1 = tkinter.Label(win,fg="#001c3d",text="加密内容: ")
    label1.pack()
    label1.config( font=('楷体',15),fg='#001c3d')
    label1.place(x=45, y=40)

    global entry3
    entry3 = tkinter.Entry(win,width=20,font=15,highlightcolor="#d4e2fc")
    entry3.pack()
    entry3.place(x=145, y=42)

    label2 = tkinter.Label(win,text="密钥: ")
    label2.pack()
    label2.config( font=('楷体',15),fg='#001c3d')
    label2.place(x=85, y=80)

    global entry4
    entry4=tkinter.Entry(win,width=20,font=3)
    entry4.pack()
    entry4.place(x=145, y=82)

    button1 = tkinter.Button(win, text="确定", width=10, height=1,background="#dcd0ff",command=get_info_en)
    button1.pack()   #加载到窗体
    button1.place(x=160, y=180)  #设置坐标（以程序界面大小为基准)

def get_info_cn():
    p = entry5.get()         #            英文内容
    K = entry6.get()         #            密钥
    print(p,K)
    q = ""
    for x in p:
        a = S_des.to_10_2_16(char_to_ascii(x))
        print("H",a)
        ab = S_des.end(a[:8], K)
        print("H", ab)
        b = S_des.to_2_10(ab)
        print("H", b)
        y = ascii_to_char(b)
        print("H", y)
        q = q + y
        print("H", q)
        ab = S_des.end(a[8:], K)
        print("H", ab)
        b = S_des.to_2_10(ab)
        print("H", b)
        y = ascii_to_char(b)
        print("H", y)
        q = q + y
        print("H", q)
    print(q)
    show(q)

def show_4():
    win = tkinter.Tk() #构造窗体
    win.title("S-DES(中文)")#标题
    '''
    400x200+400+300
    分别对应: 
    400宽度
    200高度
    300(x坐标,即横坐标,作用是设置出现的程序界面位于屏幕的哪个位置[左或者右])
    310(y坐标,即纵坐标,作用是设置出现的程序界面位于屏幕的哪个位置[上或者下])
    '''
    win.geometry("400x250+550+300")  #设置窗口的大小,具体方法在上面的注释已说明

    label1 = tkinter.Label(win,fg="#001c3d",text="加密内容: ")
    label1.pack()
    label1.config( font=('楷体',15),fg='#001c3d')
    label1.place(x=45, y=40)

    global entry5
    entry5 = tkinter.Entry(win,width=20,font=15,highlightcolor="#d4e2fc")
    entry5.pack()
    entry5.place(x=145, y=42)

    label2 = tkinter.Label(win,text="密钥: ")
    label2.pack()
    label2.config( font=('楷体',15),fg='#001c3d')
    label2.place(x=85, y=80)

    global entry6
    entry6=tkinter.Entry(win,width=20,font=3)
    entry6.pack()
    entry6.place(x=145, y=82)

    button1 = tkinter.Button(win, text="确定", width=10, height=1,background="#dcd0ff",command=get_info_cn)
    button1.pack()   #加载到窗体
    button1.place(x=160, y=180)  #设置坐标（以程序界面大小为基准)

print(rand())

win0 = tkinter.Tk() #构造窗体
win0.title("S-DES")#标题
win0.geometry("400x250+550+300")  #设置窗口的大小,具体方法在上面的注释已说明
image = Image.open("img_2.png")  # 替换为你的背景图片路径
resized_image = image.resize((400, 250), Image.ANTIALIAS)  # 调整图片尺寸为需要的大小
canvas = tkinter.Canvas(win0, width=400, height=250)  # 根据调整后的图片尺寸设置画布大小
canvas.pack()
bg_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(0, 0, anchor=NW, image=bg_image)


button1 = tkinter.Button(win0, text="输入内容加密：二进制", width=20, height=1,background="#d4e2fc",command=show_2)
button1.pack()   #加载到窗体
button1.place(x=120, y=50)  #设置坐标（以程序界面大小为基准)

button2 = tkinter.Button(win0, text="输入内容加密：英文", width=20, height=1,background="#d4e2fc",command=show_3)
button2.pack()   #加载到窗体
button2.place(x=120, y=110)  #设置坐标（以程序界面大小为基准)

button3 = tkinter.Button(win0, text="输入内容加密：中文", width=20, height=1,background="#d4e2fc",command=show_4)
button3.pack()   #加载到窗体
button3.place(x=120, y=170)  #设置坐标（以程序界面大小为基准)

#进入消息循环机制
win0.mainloop()
