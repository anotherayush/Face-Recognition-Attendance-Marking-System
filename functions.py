import customtkinter as ctk

def teammem():
    top=ctk.CTk()
    top.geometry("200x150")
    fframe= ctk.CTkFrame(top,height=100,width=100)
    fframe.pack(padx=20,pady=20)  
    top.mainloop()
i= True
def switch_event():
  global i
  if i:
    ctk.set_appearance_mode("light")
    i=False
  else:
    ctk.set_appearance_mode('dark')
    i=True
