#בס"ד
from tkinter.filedialog import askopenfilename
import imageio

import matplotlib.pyplot as plt

import cv2
import numpy as np
from tkinter import *
import math

class MyWindow:
    def __init__(self,win,img):
        self.bcd=Label(win,text="בס''ד")
        self.g=Label(win,text="בעת לחיצה ימנית על העכבר ישתנה גון התמונה")

        self.btn1=Button(win,text="בחירת תמונה",width=12)
        self.btn2=Button(win,text="הצגה",width=12)
        self.btn3=Button(win,text="הוספה",width=12)
        self.btn4=Button(win,text="מסגרת",width=12)
        self.btn5=Button(win,text="צורה",width=12)
        self.btn6=Button(win,text="שמירה ויציאה",width=12)

        self.btn2_1 = Button(win, text="מקורי",width=15)
        self.btn2_2 = Button(win, text="מטושטש",width=15)
        self.btn2_3 = Button(win, text="גווני אפור",width=15)
        self.btn2_4 = Button(win, text="שחור לבן 1",width=15)
        self.btn2_5 = Button(win, text="שחור לבן 2",width=15)
        self.l_view2= Label(win, text="בחרו כיצד תוצג התמונה שלכם")
        self.l_view= Label(win, text="כיצד התמונה תוצג אך ללא השינויים")
        self.btn2_6 = Button(win, text="מטושטש",width=15)
        self.btn2_7 = Button(win, text="גווני אפור",width=15)
        self.btn2_8 = Button(win, text="שחור לבן 1",width=15)
        self.btn2_9 = Button(win, text="שחור לבן 2",width=15)

        self.btn3_1 = Button(win, text="טקסט",width=15)
        self.entr=Entry(win,width=18)
        self.disList = Listbox(win, selectmode=EXTENDED,height=6)
        self.btn3_2 = Button(win, text="צייר מלבן",width=15)
        self.btn3_3 = Button(win, text="צייר עיגול",width=15)
        self.btn3_4 = Button(win, text="עיגול",width=15)
        self.btn3_5 = Button(win, text="מלבן",width=15)
        self.btn3_6 = Button(win, text="איקס",width=15)
        self.l_add = Label(win, text="בחרו היכן יונח האובייקט ואז לחצו על עיגול/מלבן/טקסט, אם לא תבחרו מיקום, ברירת המחדל היא למעלה")
        self.l_add2 = Label(win, text="בכל פעם בה תרצו לצייר לחצו שוב על הכפתור המתאים")

        self.btn4_1_dashed = Button(win, text="מנוקד",width=15)
        self.btn4_2_solid = Button(win, text="רגיל",width=15)
        self.lbl4_1 = Label(win, text="עובי")
        self.lbl4_2=Label(win,text="צבע")
        self.l_border = Label(win, text="בחרו עובי וצבע, ואז לחצו על מנוקד/רגיל, ניתן לשלב כמה פעמים ליצירת מסגרת מעניינת, ב''מ כחול בעובי 4")

        self.btn5_1= Button(win, text="חיתוך",width=15)
        self.btn5_2= Button(win, text="היפוך",width=15)
        self.btn5_3= Button(win, text="מראה",width=15)
        self.btn5_4= Button(win, text="סיבוב",width=15)
        self.l_cut = Label(win,text="בחרו בצורה בה תרצו לעצב את התמונה שלכם")

        self.colorsList = Listbox(win, selectmode=EXTENDED,height=8)
        self.colors = {"red":(0,0,255),"blue":(255,0,0), "pink":(186,117,255),
                       "green":(168,255,168), "yellow":(128,255,255),
                       "black":(0,0,0),"white":(255,255,255),"purple":(245,137,210)}
        self.numList = Listbox(win, selectmode=EXTENDED,height=10)
        self.disList = Listbox(win, selectmode=EXTENDED, height=3)


        self.img=img
        self.tmp=img
        self.color=(255,0,0)
        self.w=int(4)
        self.dis=(350,50)
        self.setImg()
        self.position()
        self.listim()
        self.events()
        cv2.imshow("img",self.img)

        cv2.setMouseCallback("img", self.p)
    def position(self):
        self.bcd.place(x=530,y=0)
        self.g.place(x=10,y=690)
        self.btn1.place(x=480,y=20)#choose image
        self.btn2.place(x=385,y=20)#design
        self.btn3.place(x=290,y=20)#add
        self.btn4.place(x=195,y=20)#border
        self.btn5.place(x=100,y=20)#size
        self.btn6.place(x=5,y=20)#save

    def setImg(self):
        self.img = cv2.imread(self.img)
        self.img = cv2.resize(self.img, (700, 500))
        self.tmp = cv2.imread(self.tmp)#התמונה ללא שינויים
        self.tmp = cv2.resize(self.tmp, (700, 500))

    def events(self):
       self.btn1.bind('<Button-1>', self.btn1ChooseImage)
       self.btn2.bind('<Button-1>', self.btn2Design)
       self.btn3.bind('<Button-1>', self.btn3Add)
       self.btn4.bind('<Button-1>', self.btn4Border)
       self.btn5.bind('<Button-1>', self.btn5Size)
       self.btn6.bind('<Button-1>', self.btn6Save)

       self.btn2_1.bind('<Button-1>',self.setDes1)
       self.btn2_2.bind('<Button-1>',self.setDes2)
       self.btn2_3.bind('<Button-1>',self.setDes3)
       self.btn2_4.bind('<Button-1>',self.setDes4)
       self.btn2_5.bind('<Button-1>',self.setDes5)
       self.btn2_6.bind('<Button-1>',self.setDes6)
       self.btn2_7.bind('<Button-1>',self.setDes7)
       self.btn2_8.bind('<Button-1>',self.setDes8)
       self.btn2_9.bind('<Button-1>',self.setDes9)

       self.btn3_1.bind('<Button-1>', self.addText)
       self.disList.bind('<ButtonRelease-1>', self.setDis)
       self.btn3_2.bind('<Button-1>', self.drawRectangle)
       self.btn3_3.bind('<Button-1>', self.drawCircle)
       self.btn3_4.bind('<Button-1>', self.addCircle)
       self.btn3_5.bind('<Button-1>', self.addRectangle)
       self.btn3_6.bind('<Button-1>', self.addX)

       self.btn4_1_dashed.bind('<Button-1>', self.addDashed)
       self.btn4_2_solid.bind('<Button-1>', self.addSolid)
       self.numList.bind('<ButtonRelease-1>',self.setW)
       self.colorsList.bind('<ButtonRelease-1>',self.setColor)

       self.btn5_1.bind('<Button-1>', self.cut)
       self.btn5_2.bind('<Button-1>', self.flip)
       self.btn5_3.bind('<Button-1>', self.miror)
       self.btn5_4.bind('<Button-1>', self.trans)

       self.btn6.bind('<Button-1>', self.btn6Save)


    def listim(self):
        for k in self.colors.keys():
            self.colorsList.insert(END, k)
        num = [ 2.5, 3, 3.5, 4,4.5,5,6, 8, 10, 15]
        for item in num:
            self.numList.insert(END, item)
        dis = ["למעלה", "באמצע", "למטה"]
        for item in dis:
            self.disList.insert(END, item)

    def clear(self):
        self.btn2_1.place(x=90000, y=90000)
        self.btn2_2.place(x=90000, y=90000)
        self.btn2_3.place(x=90000, y=90000)
        self.btn2_4.place(x=90000, y=90000)
        self.btn2_5.place(x=90000, y=90000)
        self.btn2_6.place(x=90000, y=90000)
        self.btn2_7.place(x=90000, y=90000)
        self.btn2_8.place(x=90000, y=90000)
        self.btn2_9.place(x=90000, y=90000)

        self.btn3_1.place(x=90000, y=90000)
        self.entr.place(x=90000, y=90000)
        self.btn3_2.place(x=90000, y=90000)
        self.disList.place(x=90000, y=90000)
        self.btn3_3.place(x=90000, y=90000)
        self.btn3_4.place(x=90000, y=90000)
        self.btn3_5.place(x=90000, y=90000)
        self.btn3_6.place(x=90000, y=90000)

        self.numList.place(x=90000, y=90000)
        self.colorsList.place(x=90000, y=90000)
        self.btn4_1_dashed.place(x=90000, y=90000)
        self.btn4_2_solid.place(x=90000, y=90000)
        self.lbl4_1.place(x=90000, y=90000)
        self.lbl4_2.place(x=90000, y=90000)

        self.btn5_1.place(x=90000, y=90000)
        self.btn5_2.place(x=90000, y=90000)
        self.btn5_3.place(x=90000, y=90000)
        self.btn5_4.place(x=90000, y=90000)

        self.l_cut.place(x=90000,y=90000)
        self.l_border.place(x=90000,y=90000)
        self.l_add.place(x=90000,y=90000)
        self.l_add2.place(x=90000,y=90000)
        self.l_view.place(x=90000,y=90000)
        self.l_view2.place(x=90000, y=90000)

    def btn2Design(self,event):
        self.clear()
        self.l_view.place(x=210,y=120)
        self.btn2_1.place(x=250,y=150)
        self.btn2_2.place(x=250,y=180)
        self.btn2_3.place(x=250,y=210)
        self.btn2_4.place(x=250,y=240)
        self.btn2_5.place(x=250,y=270)

        self.l_view2.place(x=220, y=470)
        self.btn2_6.place(x=250, y=500)
        self.btn2_7.place(x=250, y=530)
        self.btn2_8.place(x=250, y=560)
        self.btn2_9.place(x=250, y=590)

    def btn1ChooseImage(self, event):
        self.clear()
        file_name = askopenfilename()
        self.img=imageio.imread(file_name)
        self.img = cv2.resize(self.img, (700, 500))
        #self.img = cv2.imread(self.img)
        self.tmp=self.img # התמונה ללא שינויים

        cv2.imshow("img",self.img)

    def btn3Add(self, event):
        self.clear()
        self.l_add.place(x=10,y=81)
        self.l_add2.place(x=120,y=101)
        self.btn3_1.place(x=250,y=150)
        self.entr.place(x=250,y=180)

        self.btn3_2.place(x=250,y=230)
        self.btn3_3.place(x=250,y=270)
        self.btn3_4.place(x=250,y=310)
        self.btn3_5.place(x=250,y=350)
        self.btn3_6.place(x=250,y=390)

        self.disList.place(x=250, y=420)

    def btn4Border(self, event):
        self.clear()
        self.l_border.place(x=10,y=81)
        self.numList.pack()
        self.lbl4_1.place(x=250, y=130)
        self.numList.place(x=250, y=150)

        self.colorsList.pack()
        self.lbl4_2.place(x=250, y=340)
        self.colorsList.place(x=250, y=360)

        self.btn4_1_dashed.place(x=250, y=540)
        self.btn4_2_solid.place(x=250, y=570)

    def btn5Size(self, event):
        self.clear()
        self.l_cut.place(x=210,y=81)
        self.btn5_1.place(x=250,y=150)
        self.btn5_2.place(x=250,y=180)
        self.btn5_3.place(x=250,y=210)
        self.btn5_4.place(x=250,y=240)

    def btn6Save(self, event):
        cv2.destroyAllWindows()
        cv2.imwrite('yourImage.png', self.img)
        cv2.destroyAllWindows()
        sys.exit()


    def setDes1(self,event):
        self.img=self.tmp
        cv2.imshow("img", self.tmp)
    def setDes2(self,event):
         self.img=cv2.GaussianBlur(self.tmp,(7,7),0)
         cv2.imshow("img",self.img)
    def setDes3(self, event):
       self.img=cv2.cvtColor(self.tmp,cv2.COLOR_BGR2GRA)
       cv2.imshow("img", self.img)
    def setDes4(self,event):
        self.img=cv2.Canny(self.tmp,200,300)
        cv2.imshow("img", self.img)
    def setDes5(self,event):
        self.img=cv2.dilate(cv2.Canny(self.tmp,200,300),np.ones((5,5),dtype=np.uint8),iterations=1)
        cv2.imshow("img", self.img)
    def setDes6(self,event):
         self.img=cv2.GaussianBlur(self.img,(7,7),0)
         cv2.imshow("img",self.img)
    def setDes7(self, event):
       self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
       cv2.imshow("img", self.img)
    def setDes8(self,event):
        self.img=cv2.Canny(self.img,200,300)
        cv2.imshow("img", self.img)
    def setDes9(self,event):
        self.img=cv2.dilate(cv2.Canny(self.img,200,300),np.ones((5,5),dtype=np.uint8),iterations=1)
        cv2.imshow("img", self.img)


    def addText(self,event):
        cv2.putText(self.img, self.entr.get(),self.dis , cv2.FONT_HERSHEY_PLAIN, 3.5, (255, 0, 50), 4)
        cv2.imshow("img",self.img)

    ix = 0
    iy = 0
    jx = 0
    jy = 0
    drawing = False

    def drawRectangle(self,event):
        cv2.setMouseCallback("img", self.toDrawRect)

    def toDrawRect(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix=x
            self.iy=y
        elif event==cv2.EVENT_MOUSEMOVE:
            self.jx=x
            self.jy=y
        elif event==cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.img,(self.ix,self.iy),(self.jx,self.jy),(0,0,40),-1)
            cv2.imshow("img",self.img)
            cv2.setMouseCallback("img", self.p)

    def addRectangle(self,event):
        cv2.rectangle(self.img,(10,int(self.dis[1]-40)),(self.img.shape[1]-10,int(self.dis[1])),(20,0,0),2)
        cv2.imshow("img", self.img)

    def drawCircle(self, event):
        cv2.setMouseCallback("img", self.toDrawCircle)

    def toDrawCircle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_MOUSEMOVE:
            self.jx = x
            self.jy = y
        elif event == cv2.EVENT_LBUTTONUP:
            xx = int((self.ix + self.jx) / 2)
            yy = int((self.iy + self.jy) / 2)
            r = int(math.sqrt(pow(self.ix - self.jx, 2) + pow(self.iy, self.jy, 2)))
            self.img = cv2.circle(self.img, (xx, yy), r, (0, 0, 255), 1)
            cv2.imshow("img", self.img)
            cv2.setMouseCallback("img", self.p)
    def addCircle(self,event):
        self.img = cv2.circle(self.img,self.dis, 20, (0, 0, 255),2)
        cv2.imshow("img", self.img)

    def addX(self,event):
        cv2.line(self.img, (0, 0), (self.img.shape[1], self.img.shape[0]), ( 0,255, 0),2, cv2.LINE_AA)
        cv2.line(self.img, (self.img.shape[1],0 ), (0,self.img.shape[0]), (0, 255, 0),2, cv2.LINE_AA)
        cv2.imshow("img", self.img)

    def addDashed(self,event):
        for y in range(5,self.img.shape[1]-5,20):
            cv2.line(self.img, (5, y), (5, y), self.color,self.w, cv2.LINE_AA)
            cv2.line(self.img, (y,5), (y,5), self.color, self.w, cv2.LINE_AA)
        for x in range(5, self.img.shape[1] - 5, 20):
            cv2.line(self.img, (self.img.shape[1] - 5,x),  (self.img.shape[1] - 5,x), self.color, self.w, cv2.LINE_AA)
            cv2.line(self.img,(x, self.img.shape[0] - 5),(x,self.img.shape[0] - 5) , self.color, self.w, cv2.LINE_AA)
        cv2.imshow("img", self.img)

    def addSolid(self,event):
        cv2.line(self.img, (5,5), (self.img.shape[1]-5,5), self.color, self.w, cv2.LINE_AA)
        cv2.line(self.img, (5, self.img.shape[0]-5), (self.img.shape[1]-5,self.img.shape[0]-5),self.color,self.w, cv2.LINE_AA)
        cv2.line(self.img, (5, 5), (5, self.img.shape[0]-5),self.color, self.w, cv2.LINE_AA)
        cv2.line(self.img, (self.img.shape[1]-5, 5), (self.img.shape[1]-5,self.img.shape[0]-5), self.color,self.w, cv2.LINE_AA)
        cv2.imshow("img", self.img)

    def cut(self,event):
        cv2.setMouseCallback("img", self.toCut)

    def toCut(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_MOUSEMOVE:
            self.jx = x
            self.jy = y
        elif event == cv2.EVENT_LBUTTONUP:
            self.img=self.img[self.iy:self.jy,self.ix:self.jx]
            cv2.imshow("img",self.img)
            cv2.setMouseCallback("img", self.p)

    def flip(self,event):
        self.img=cv2.flip(self.img,-1)
        cv2.imshow("img", self.img)
    def miror(self,event):
        self.img=cv2.flip(self.img,1)
        cv2.imshow("img", self.img)
    def trans(self,event):
        self.img=cv2.transpose(self.img,0)
        cv2.imshow("img", self.img)

    def setColor(self,event):
        index = self.colorsList.curselection()[0]
        self.color= self.colors.get(self.colorsList.get(index))

    def setW(self,event):
        index = self.numList.curselection()[0]
        self.w =int(self.numList.get(index))

    def setDis(self,event):
        index = self.disList.curselection()[0]
        tmp=[50,(self.img.shape[0]/2),(self.img.shape[0]-30)]
        self.dis = (int((self.img.shape[1])/2),int(tmp[index]))

    def p(self,event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDOWN:
            self.img=cv2.cvtColor(self.img,cv2.COLOR_XYZ2BGR)
            cv2.imshow("img", self.img)



window=Tk()
mywin=MyWindow(window,"P1110773.JPG")
window.geometry("580x720+920+30")
window.mainloop()
