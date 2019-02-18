# !/usr/bin/env python
# coding=utf-8
'''
date:2018/07
'''
import  tkinter
import threading
import  time
root=tkinter.Tk()
root.title('那年我们追过的女神')
root.minsize(300,300)
bn1=tkinter.Button(root,text='1号',bg='red')
bn1.place(x=20,y=20,width=50,height=50)

bn2=tkinter.Button(root,text='2号',bg='white')
bn2.place(x=90,y=20,width=50,height=50)

bn3=tkinter.Button(root,text='3号',bg='white')
bn3.place(x=160,y=20,width=50,height=50)

bn4=tkinter.Button(root,text='娇娇',bg='white')
bn4.place(x=230,y=20,width=50,height=50)

bn5=tkinter.Button(root,text='5号',bg='white')
bn5.place(x=230,y=90,width=50,height=50)

bn6=tkinter.Button(root,text='6号',bg='white')
bn6.place(x=230,y=160,width=50,height=50)

bn7=tkinter.Button(root,text='娇娇',bg='white')
bn7.place(x=230,y=230,width=50,height=50)

bn8=tkinter.Button(root,text='8号',bg='white')
bn8.place(x=160,y=230,width=50,height=50)

bn9=tkinter.Button(root,text='9号',bg='white')
bn9.place(x=90,y=230,width=50,height=50)

bn10=tkinter.Button(root,text='娇娇',bg='white')
bn10.place(x=20,y=230,width=50,height=50)

bn11=tkinter.Button(root,text='10号',bg='white')
bn11.place(x=20,y=160,width=50,height=50)

bn12=tkinter.Button(root,text='11号',bg='white')
bn12.place(x=20,y=90,width=50,height=50)

gilrlists=[bn1,bn2,bn3,bn4,bn5,bn6,bn7,bn8,bn9,bn10,bn11,bn12]
#定义是否开启循环的标志位
isloop=False

#停止的标记

stopsign=False

#通过id的索引值来确定对应的选项
stopid=None
#目的 1 循环我们的被选项 2 设置选项的背景颜色
def round():
    global isloop
    global stopid
    #判断是否开启循环了
    if isloop==True:  #用来判断按键是否按下，如果按下了再按则无效 return 开始为false 进入下面，如果为true，立马返回。
        return
    i=1
    if isinstance(stopid,int):
        i=stopid
    # 开始循环
    while True:
        time.sleep(0.05)
        for x in gilrlists:
            x['bg']='white'
        gilrlists[i]['bg']='red'
        i+=1
        if i >= len(gilrlists):
            i=0
        if stopsign==True: # 停止状态下的变量
            isloop=False
            stopid=i
            break
def stop():
    global stopsign
    if stopsign==True:
        return
    stopsign=True
def newtask():
    global isloop
    global stopsign
    stopsign=False
    #建立线程
    #Thread 线程类 2种方法：1直接传入要运行的方法 2 继承并覆盖run（）
    #groub 线程组 一般默认为None
    #name 线程名
    # args/kwargs 要传入方法的参数
    t=threading.Thread(target=round)
    #开启线程
    t.start()
    isloop=True#必须写在后面 启动线程时要isloop为false，进入while true：后isloop为true，除非停止，才变成false

btn_start=tkinter.Button(root,text='开始',bg='white',command=newtask)
btn_start.place(x=90,y=120,width=50,height=50)
btn_stop=tkinter.Button(root,text='停止',bg='white',command=stop)
btn_stop.place(x=160,y=120,width=50,height=50)

root.mainloop()
