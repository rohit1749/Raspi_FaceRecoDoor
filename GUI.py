from tkinter import *                   # imports the Tkinter lib
from subprocess import call
import os,sys
from tkinter import filedialog
root = Tk()				# create the root object
root.wm_title("Face Recognition")	# sets title of the window
root.configure(bg="#55c8f2")		# change the background color 
root.attributes("-fullscreen", True) 	# set to fullscreen

def opencallback():
     os.system('python3 capture.py')

def openFile():
    filepath=filedialog.askopenfilename(initialdir="/home/Pi/Face/opencv-face-recognition/face-detection",)            
    file=open(filepath,'r')
    print(file.read())
    file.close()

label_1 = Label(root, text="Welcome to FaceRecoDoor", font="Verdana 26 bold",
			fg="#470a0a")

#Add a button inside the window
Button_1=Button(root, text = "Capture", command = opencallback) 
Button_2= Button(root, text="Train",command = openFile)
Button_3= Button(root, text="Recognise",command = openFile)


label_1.grid(row=0, column=0)

Button_1.grid(row=1, column=0)
Button_2.grid(row=2, column=0)
Button_3.grid(row=5, column=0)

# we can exit when we press the escape key
def end_fullscreen(event):
	root.attributes("-fullscreen", False)



root.bind("<Escape>", end_fullscreen)
root.mainloop()		
