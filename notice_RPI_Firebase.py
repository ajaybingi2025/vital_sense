from tkinter import *
import cv2
import time
from PIL import ImageTk, Image
from firebase import firebase

root = Tk()
root.title("Basic GUI Layout")

root.maxsize(900, 600)  

root.config(bg="skyblue") 

cap = cv2.VideoCapture('bridge.mp4')
time.sleep(2)
kk=0
firebase = firebase.FirebaseApplication('https://milk-d6036-default-rtdb.firebaseio.com/', None)
def vid():
    
        
        _,frame=cap.read()
        
        frame = cv2.resize(frame, (600,380))
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        root.after(1, vid)

def display():
    
        
##        _,frame=cap.read()
##        
##        frame = cv2.resize(frame, (600,380))
##        img = Image.fromarray(frame)
##        imgtk = ImageTk.PhotoImage(image=img)
##        lmain.imgtk = imgtk
##        lmain.configure(image=imgtk)
##        #Label(right_frame, image=img).grid(row=0,column=0, padx=5, pady=5)

        global kk
        kk=kk+1
        ece_nts1=firebase.get('/NRI_NOTICE_BOARD', '/ECE/1')
        ece_nts2=firebase.get('/NRI_NOTICE_BOARD', '/ECE/2')
        ece_nts3=firebase.get('/NRI_NOTICE_BOARD', '/ECE/3')
        #ece_nts4="WELCOME"

        
        Label(ece_bar, text=ece_nts1).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(ece_bar, text=ece_nts2).grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(ece_bar, text=ece_nts3).grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        #Label(ece_bar, text=ece_nts4).grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget


        eee_nts1=firebase.get('/NRI_NOTICE_BOARD', '/EEE/1')
        eee_nts2=firebase.get('/NRI_NOTICE_BOARD', '/EEE/2')
        eee_nts3=firebase.get('/NRI_NOTICE_BOARD', '/EEE/3')
        #eee_nts4="WELCOME"
        
        Label(eee_bar, text=eee_nts1).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(eee_bar, text=eee_nts2).grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(eee_bar, text=eee_nts3).grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        #Label(eee_bar, text=eee_nts4).grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget


        cse_nts1=firebase.get('/NRI_NOTICE_BOARD', '/CSE/1')
        cse_nts2=firebase.get('/NRI_NOTICE_BOARD', '/CSE/2')
        cse_nts3=firebase.get('/NRI_NOTICE_BOARD', '/CSE/3')
        

        
        Label(cse_bar, text=cse_nts1).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(cse_bar, text=cse_nts2).grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(cse_bar, text=cse_nts3).grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        #Label(cse_bar, text=cse_nts4).grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget


        it_nts1=firebase.get('/NRI_NOTICE_BOARD', '/IT/1')
        it_nts2=firebase.get('/NRI_NOTICE_BOARD', '/IT/2')
        it_nts3=firebase.get('/NRI_NOTICE_BOARD', '/IT/3')
        

        
        Label(it_bar, text=it_nts1).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(it_bar, text=it_nts2).grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(it_bar, text=it_nts3).grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        #Label(it_bar, text=it_nts4).grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        flash_nts1=firebase.get('/NRI_NOTICE_BOARD', '/FLASH/1')
        Label(flash_bar, text="*    Flash Notices Display Here                *").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        
        Label(flash_bar, text=flash_nts1).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        root.after(10000, display)


app = Frame(root, bg="white")
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

lmain = Label(right_frame)
lmain.grid()

botl_frame = Frame(root, width=200, height=30, bg='grey')
botl_frame.grid(row=1, column=0, padx=10, pady=5)

botr_frame = Frame(root, width=650, height=30, bg='grey')
botr_frame.grid(row=1, column=1, padx=10, pady=5)

ece_bar = Frame(left_frame, width=180, height=90)
ece_bar.grid(row=0, column=0, padx=5, pady=5)

eee_bar = Frame(left_frame, width=180, height=90)
eee_bar.grid(row=1, column=0, padx=5, pady=5)

cse_bar = Frame(left_frame, width=180, height=90)
cse_bar.grid(row=2, column=0, padx=5, pady=5)

it_bar = Frame(left_frame, width=180, height=90)
it_bar.grid(row=3, column=0, padx=5, pady=5)

flash_bar = Frame(botr_frame, width=650, height=30)
flash_bar.grid(row=0, column=0, padx=5, pady=5)







##firebase.put("/NRI_NOTICE_BOARD", "/ECE/1", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/ECE/2", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/ECE/3", "welcome")
##
##firebase.put("/NRI_NOTICE_BOARD", "/EEE/1", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/EEE/2", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/EEE/3", "welcome")
##
##firebase.put("/NRI_NOTICE_BOARD", "/CSE/1", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/CSE/2", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/CSE/3", "welcome")
##
##
##firebase.put("/NRI_NOTICE_BOARD", "/IT/1", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/IT/2", "welcome")
##firebase.put("/NRI_NOTICE_BOARD", "/IT/3", "welcome")
##
##firebase.put("/NRI_NOTICE_BOARD", "/FLASH/1", "welcome")





# Example labels that serve as placeholders for other widgets
Label(ece_bar, text="ECE DEPARTMENT NOTICE BOARD",foreground="red").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(ece_bar, text="").grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(ece_bar, text="").grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(ece_bar, text="").grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
#Label(ece_bar, text="").grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

Label(eee_bar, text="EEE DEPARTMENT NOTICE BOARD",foreground="red").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(eee_bar, text="").grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(eee_bar, text="").grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(eee_bar, text="").grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
#Label(eee_bar, text="").grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

Label(cse_bar, text="CSE DEPARTMENT NOTICE BOARD",foreground="red").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(cse_bar, text="").grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(cse_bar, text="").grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(cse_bar, text="").grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
#Label(cse_bar, text="").grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget


Label(it_bar, text="IT DEPARTMENT NOTICE BOARD",foreground="red").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(it_bar, text="").grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(it_bar, text="").grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(it_bar, text="").grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
#Label(eee_bar, text="").grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

Label(flash_bar, text="*    Flash Notices Display Here                *").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(flash_bar, text="").grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
vid()
display()
root.mainloop()

