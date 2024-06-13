
from tkinter import *                   # imports the Tkinter lib
import os,sys
from tkinter import filedialog
from tkinter import messagebox
import time
import cv2
import numpy as np

root = Tk()				# create the root object
root.wm_title("Face Recognition")	# sets title of the window
root.configure(bg="#940A4F")		# change the background color 
#root.attributes("-fullscreen", True) 	# set to fullscreen


def opencapture():
  #  messagebox.showinfo("Assist","Click OK to start the camera!")
    
    #time.sleep(10)
    os.system('python3 capture.py')
     

def opentrain():
   os.system('python3 train.py')
   messagebox.showinfo("Assist","Training Completed!")
   
def recognise():
   os.system('python3 recognise.py')
   messagebox.showinfo("Assist","Please look into the camera to unlock the door")
   
f1=Frame(root,bg="black",borderwidth=6,relief=RAISED)
f1.pack(fill="x")
label_1 = Label(f1, text="Welcome to FaceRecoDoor", font="Verdana 26 italic",
			fg="#470a0a")
label_1.pack(fill="x")

f2=Frame(root,borderwidth=5,bg="grey")
f2.pack(pady=35)

f3=Frame(root,borderwidth=5,bg="grey")
f3.pack(pady=35)

f4=Frame(root,borderwidth=5,bg="grey")
f4.pack(pady=35)

#Add a button inside the window
Button_1=Button(f2, text = "Capture", command = opencapture,width=30,bg="yellow") 
Button_2= Button(f3, text="Train",command = opentrain,width=30,bg="red")
Button_3= Button(f4, text="Recognise",command = recognise,width=30,bg="green")
Button_1.pack()
Button_2.pack()
Button_3.pack()

#label_1.grid(row=0, column=0,sticky="NSEW")

#Button_1.grid(row=4, column=0)
#Button_2.grid(row=8, column=0)
#Button_3.grid(row=12, column=0)

# we can exit when we press the escape key
def end_fullscreen():
	root.attributes("-fullscreen", False)

Button_4= Button(root, text="Quit",width=15, command=root.destroy).pack()

#root.bind("<Escape>", end_fullscreen)
root.mainloop()		



