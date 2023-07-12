import customtkinter as ctk
import tkinter
from PIL import ImageTk,Image
import functions

root = ctk.CTk()
root.title("Attendance Marking System")
root.geometry("600x400")
ctk.set_default_color_theme("dark-blue")

img1=ImageTk.PhotoImage(Image.open("wallpaper.png"))
l1=ctk.CTkLabel(master=root,image=img1)
l1.pack()

frame=ctk.CTkFrame(master=l1, width=400, height=320, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=ctk.CTkLabel(master=frame, text="Student Attendance Marking System",font=("sans-serif", 20))
l2.place(x=40, y=40)

b1= ctk.CTkButton(master=frame,text='Mark Attendance',width=200, height=30,corner_radius=5)
b1.place(x=110,y=120)

b2= ctk.CTkButton(master=frame,text="Generate Today's Report",width=200, height=30,corner_radius=5)
b2.place(x=110,y=160)

b3= ctk.CTkButton(master=frame,text='Add New Student',width=200, height=30,corner_radius=5)
b3.place(x=110,y=200)

f2=ctk.CTkFrame(master=frame,width=280,height=50)
f2.place(x=100,y=250)

switch = ctk.CTkSwitch(f2,text="",width=0,command=functions.switch_event)
switch.grid(row=0,column=0,padx=5,pady=10)

b4= ctk.CTkButton(f2,text="Our Team",width=70,command=functions.teammem)
b4.grid(row=0,column=1,padx=5,pady=10)

def destroyy():
    root.destroy()
b5= ctk.CTkButton(f2,text="Exit",width=70,command=destroyy)
b5.grid(row=0,column=2,padx=10,pady=10)


root.mainloop()