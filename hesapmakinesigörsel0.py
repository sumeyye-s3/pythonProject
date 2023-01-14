from tkinter import *

def yaz(x):
    s = len(giriş.get())
    giriş.insert(s,str(x))
    #print(x)

s2 = 0
def hesapla():
    global s2
    s2 = float(giriş.get())
    print(s2)
    global  hesap
    sonuc=0
    if(hesap==0):
        sonuc = s1 + s2
    elif(hesap==1):
        sonuc = s1 - s2
    elif(hesap==2):
        sonuc = s1 * s2
    elif(hesap==3):
        sonuc = s1 / s2
    giriş.delete(0,'end')
    giriş.insert(0,str(sonuc))

hesap = 5
s1 = 0

def işlemler(x):
    global  hesap
    hesap = x
    global s1
    s1 = float(giriş.get())
    print(hesap)
    print(s1)
    giriş.delete(0,'end')

pencere= Tk()
pencere.geometry("250x250")

giriş = Entry(font="verdana 14 bold",fg="RED" ,width=15,justify=RIGHT)
giriş.place(x=20,y=20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),fg= "GREEN" ,font="Verdana 14 bold",command=lambda x=i:yaz(x)))

sayac=0
for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1

işlem = []
for i in range(0,4):
    işlem.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:işlemler(x)))

işlem[0]['text'] = "+"
işlem[1]['text'] = "-"
işlem[2]['text'] = "*"
işlem[3]['text'] = "/"



for i in range(0,4):
    işlem[i].place(x=170,y=50+50*i)

sb = Button(text=0,font="Verdana 14 bold",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)

nb = Button(text=".",font="Verdana 14 bold",width=2,command=lambda x=".":yaz(x))
nb.place(x=70,y=200)

eb = Button(text='=',fg= "BLUE",font="Verdana 14 bold",width=2,command=hesapla)
eb.place(x=120,y=200)
pencere.mainloop()

