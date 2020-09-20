from tkinter import *
from PIL import Image,ImageTk

wind3=Tk()
wind3.geometry('700x600')

#-------Image-section-------

image=Image.open("C:\\Users\\Rucha\\Desktop\\My Stuff\\sk4.jpg")
photo=ImageTk.PhotoImage(image)
lbl=Label(wind3,image=photo)
lbl.pack(padx=0,pady=0)

#----function----
def calculate1():
    Face_Wash=e1.get()
    Face_Mask=e2.get()
    Cleanser=e3.get()
    Skin_oil=e4.get()
    Lip_Mask=e5.get()
    Sunblock=e6.get()
    Scrub=e7.get()
    Night_Gel=e8.get()
    Face_Serum=e9.get()
    Body_Lotion=e10.get()
    Lip_Balm=e11.get()
    Hair_Oil=e12.get()
    Shampoo=e13.get()
    Conditioner=e14.get()
    Serum =e15.get()
    Hair_Mask =e16.get()
    Hair_Color =e17.get()
    Hair_Lotion =e18.get()
    Hair_Cream =e19.get()
    Hair_Mousse =e20.get()
    Hair_Spray =e21.get()
    Hair_Wax= e22.get()



    total=((int(Face_Wash)*75)+(int(Face_Mask)*100)+(int(Cleanser)*120)+(int(Skin_oil)*450)+(int(Lip_Mask)*430)+(int(Sunblock)*494)+(int(Scrub)*150)+(int(Night_Gel)*460)+(int(Face_Serum)*595)+(int(Body_Lotion)*295)+(int(Lip_Balm)*150)+(int(Hair_Oil)*200)+(int(Shampoo)*450)+(int(Conditioner)*300)+(int(Serum)*200)+(int(Hair_Mask)*500)+(int(Hair_Color)*350)+(int(Hair_Lotion)*690)+(int(Hair_Cream)*820)+(int(Hair_Mousse)*720)+(int(Hair_Spray)*270)+(int(Hair_Wax)*490))

    label60 = Label(wind3, text='TOTAL BILL:{}'.format(total), font="times 18")
    label60.place(x=220, y=560)

#-----label section----

label99 = Label(wind3, text='RUCHA BEAUTY PRODUCTS', font="times 20 bold ")
label99.place(x=130, y=10)


#----SKin Care Products----

label100 = Label(wind3, text='Skin Care Products', font="times 15 bold ")
label100.place(x=20, y=50)

label1 = Label(wind3, text='Hair Oil            Rs 200', font="times 10 bold ")
label1.place(x=450, y=90)
e12 = Entry(wind3)
e12.insert(0, int(0))
e12.place(x=450, y=110)

label2=Label(wind3,text='Shampoo           Rs 450',font="times 10 bold ")
label2.place(x=450,y=130)
e13=Entry(wind3)
e13.insert(0,int(0))
e13.place(x=450,y=150)

label3=Label(wind3,text='Conditioner     Rs 300',font="times 10 bold")
label3.place(x=450,y=170)
e14=Entry(wind3)
e14.insert(0,int(0))
e14.place(x=450,y=190)

label4=Label(wind3,text='Serum              Rs 200',font="times 10 bold")
label4.place(x=450,y=210)
e15=Entry(wind3)
e15.insert(0,int(0))
e15.place(x=450,y=230)

label5=Label(wind3,text='Hair Mask       Rs 560',font="times 10 bold")
label5.place(x=450,y=250)
e16=Entry(wind3)
e16.insert(0,int(0))
e16.place(x=450,y=270)

label6=Label(wind3,text='Hair Color        Rs 350',font="times 10 bold")
label6.place(x=450,y=290)
e17=Entry(wind3)
e17.insert(0,int(0))
e17.place(x=450,y=310)

label7=Label(wind3,text='Hair Lotion      Rs 690',font="times 10 bold")
label7.place(x=450,y=330)
e18=Entry(wind3)
e18.insert(0,int(0))
e18.place(x=450,y=350)

label8=Label(wind3,text='Hair Cream     Rs 820',font="times 10 bold")
label8.place(x=450,y=370)
e19=Entry(wind3)
e19.insert(0,int(0))
e19.place(x=450,y=390)

label9 = Label(wind3, text='Hair Mousse   Rs 720', font="times 10 bold ")
label9.place(x=450, y=410)
e20 = Entry(wind3)
e20.insert(0, int(0))
e20.place(x=450, y=430)

label10 = Label(wind3, text='Hair Spray      Rs 270', font="times 10 bold ")
label10.place(x=450, y=450)
e21 = Entry(wind3)
e21.insert(0, int(0))
e21.place(x=450, y=470)

label11 = Label(wind3, text='Hair Wax         Rs 490', font="times 10 bold ")
label11.place(x=450, y=490)
e22 = Entry(wind3)
e22.insert(0, int(0))
e22.place(x=450, y=510)



#---------Hair Care Products------------

label101 = Label(wind3, text='Hair Care Products', font="times 15 bold ")
label101.place(x=450, y=50)

label16 = Label(wind3, text='Face Wash         Rs 75', font="times 10 bold ")
label16.place(x=20, y=90)
e1 = Entry(wind3)
e1.insert(0, int(0))
e1.place(x=20, y=110)

label17=Label(wind3,text='Face Mask       Rs 100',font="times 10 bold ")
label17.place(x=20,y=130)
e2=Entry(wind3)
e2.insert(0,int(0))
e2.place(x=20,y=150)

label18=Label(wind3,text='Cleanser          Rs 120',font="times 10 bold")
label18.place(x=20,y=170)
e3=Entry(wind3)
e3.insert(0,int(0))
e3.place(x=20,y=190)

label19=Label(wind3,text='Facial Oil        Rs 450',font="times 10 bold")
label19.place(x=20,y=210)
e4=Entry(wind3)
e4.insert(0,int(0))
e4.place(x=20,y=230)

label20=Label(wind3,text='Sleep Mask     Rs 430',font="times 10 bold")
label20.place(x=20,y=250)
e5=Entry(wind3)
e5.insert(0,int(0))
e5.place(x=20,y=270)

label21=Label(wind3,text='Sunblock         Rs 494',font="times 10 bold")
label21.place(x=20,y=290)
e6=Entry(wind3)
e6.insert(0,int(0))
e6.place(x=20,y=310)

label22=Label(wind3,text='Scrub               Rs 150',font="times 10 bold")
label22.place(x=20,y=330)
e7=Entry(wind3)
e7.insert(0,int(0))
e7.place(x=20,y=350)

label23=Label(wind3,text='Night Gel         Rs 460',font="times 10 bold")
label23.place(x=20,y=370)
e8=Entry(wind3)
e8.insert(0,int(0))
e8.place(x=20,y=390)

label24 = Label(wind3, text='Face Serum     Rs 595', font="times 10 bold ")
label24.place(x=20, y=410)
e9 = Entry(wind3)
e9.insert(0, int(0))
e9.place(x=20, y=430)

label25 = Label(wind3, text='Body Lotion     Rs 295', font="times 10 bold ")
label25.place(x=20, y=450)
e10 = Entry(wind3)
e10.insert(0, int(0))
e10.place(x=20, y=470)

label25 = Label(wind3, text='Lip Balm          Rs 150', font="times 10 bold ")
label25.place(x=20, y=490)
e11 = Entry(wind3)
e11.insert(0, int(0))
e11.place(x=20, y=510)



#------button-------
b1=Button(wind3,text='Bill',width=25,command=calculate1,fg='blue')
b1.place(x=220,y=530)

wind3.mainloop()