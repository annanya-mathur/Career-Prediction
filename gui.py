# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from tkinter import *


df=pd.read_csv('exams (2).csv')


X=df[['aptitude score','test preparation course']]
Y = df[['GradePoints']]

X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.3)

rf=RandomForestRegressor()
model=rf.fit(np.array(X_train).reshape(-1,2),np.array(Y_train).reshape(-1,1))

main_window= Tk()

main_window.geometry('1100x600')

v1=StringVar()
v2=StringVar()


# labels for displaying output
Label(main_window , font=("Arial", 20),text="This interface will provide many Career Options for the students based on there aptitude").pack(pady=40)
Label(main_window ,font=("Arial", 15), text="Enter aptitude score out of 100").pack(pady=10)
my_apt=Entry(main_window,font=("Arial", 15),textvariable=v1 ,width=50 ,borderwidth=5)
my_apt.pack()
Label(main_window ,font=("Arial", 15), text="Have you completed test preparation say 1 for yes & 0 for no ").pack(pady=10)
my_test=Entry(main_window, font=("Arial", 15),textvariable =v2,width=50 ,borderwidth=5)
my_test.pack()



def on_click():
    try:
        n_apt=int(my_apt.get())
        n_test=int(my_test.get())
        print(n_test)
        a=n_apt
        b=n_test
        Label(main_window , font=("Arial", 20),text="Predicted Career Choices",foreground='red').pack()
        r=np.array(rf.predict(np.array([[a,b]])))
        print(r)
        if r>=0.9 and r<=1.0 :
            Label(main_window, font=("Copperplate Gothic Bold",15),text="⦿Medical    ⦿ Engineering      ⦿Management        ⦿Mathematician       ⦿Lawyer  ⦿Data Scientist    ⦿Mobile Application Developer").pack()
            Label(main_window,font=("Copperplate Gothic Bold",15),text="⦿Pharmacy    ⦿ Executive Director      ⦿Researcher     ⦿AI/ML Specialist      ⦿Professor    ⦿Bioinformatics    ⦿Chartered Accountancy").pack()
        if (r >=0.7 and r<=0.9) or (r>=0.9 and r<=1.0):
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿HR    ⦿Teaching Assistant    ⦿Sound Engineering    ⦿Sports Officer    ⦿Content Writer    ⦿Brand Analyst    ⦿Campus Ambassador").pack()
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Lab Assistant   ⦿3-D Modelling   ⦿Web Development    ⦿Finance     ⦿Editor    ⦿Associate   ⦿Digital Sculptor    ⦿Big Data Analyst").pack()   
        if (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Sales     ⦿Center head for sports     ⦿Designer     ⦿Marketing    ⦿Pathology    ⦿Blockchain Development     ⦿Humanities    ⦿Mining").pack()
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Anchoring    ⦿Game Development    ⦿Cryptography    ⦿Program Manager    ⦿Journalism    ⦿Copy Writing    ⦿Content Production").pack()        
        if (r>=0.4 and r<=0.5) or (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Hotel Management    ⦿Milk Processing Operator    ⦿Plant Engineering    ⦿Nutritionist   ⦿Physical Education   ⦿Podcast Production").pack()
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Enterpreneur     ⦿Psychiatrist     ⦿Receptionist    ⦿Voiceover    ⦿Singing    ⦿Acting    ⦿Dietician     ⦿Culinary Arts    ⦿Choreography").pack()    
        if (r>=0.1 and r<=0.4) or (r>=0.4 and r<=0.5) or (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Ayurveda     ⦿Mountaineer     ⦿Wrestler     ⦿Archer     ⦿Coach     ⦿Chef     ⦿Caterer     ⦿Environmentalist     ⦿Event Manager").pack()
            Label(main_window,font=("Copperplate Gothic Bold",15) ,text="⦿Interior designing      ⦿Trainer      ⦿Farmer      ⦿Youtuber      ⦿Social Media Influencer      ⦿Food Processing Superviser").pack()
        
        
        
       
    except:
        answer.config(text="Not a Number")
    
    



Button (main_window,font=("Copperplate Gothic Bold", 15), text = "Submit",foreground='green',command=on_click).pack(pady=20)



answer=Label(main_window,font=("Copperplate Gothic Bold", 25),text="",foreground='red')
answer.pack()






main_window.mainloop()