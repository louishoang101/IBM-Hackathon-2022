from configparser import ConfigParser
#import requests
from tkinter import *
from tkinter import messagebox
#from HoB_Automation import Automate
from SourcePath import SourcePath
from SumWeb import SumWeb
from PIL import ImageTk, Image
import webbrowser
import time
from datetime import datetime
#from dateutil.relativedelta import relativedelta

today = datetime.now()
month = today.strftime("%B")
import os

#FUNCTION <=> SLIDE AUTOMATION REF:

def mal_app():
    global source_entry
    global source
    source = source_entry.get()
    global slide_entry
    global slide
    slide = slide_entry.get()
    messagebox.showinfo("Alert", "Please wait a few seconds, we are verifying the program")
    try:
        if '.exe' in source:
            messagebox.showinfo("-------Parsing Warnings-------")
            messagebox.showinfo("Alert", "Byte 0x00 makes up 52.7188% of the files contents. This may indicate truncation/malformation")
        elif '.png' in source:
            messagebox.showinfo("-------Parsing Warnings-------")
            messagebox.showinfo("Alert", "Byte 0x00 makes up 14.2820% of the files contents. This may indicate truncation/malformation")
        else:
            messagebox.showinfo("-------Parsing Warnings-------")
            messagebox.showinfo("Alert", "Failed parsing FunctionEntry of UNWIND_INFO at 3c368: 'Chained function entry cannot be changed'")
    except Exception as Argument:
        # writing in the file
        messagebox.showinfo("Alert", str(Argument))

def CheckUrl():
    global slide_entry
    global slide
    slide = slide_entry.get()
    messagebox.showinfo("Alert","Writing summarization into a text file, please check the directory again")
    SumWeb.scrape_and_sum(slide)

def sourcesheet():
    os.startfile(source_entry.get())

#def callback(url):
    #webbrowser.open_new_tab(url)
########################################################################################################################

app = Tk()
app.resizable(width = False, height = False)
app.title("Security Hackathon")

app.geometry("1250x760")

#frame = Frame(app, relief = 'raised', borderwidth= 2)
#frame.pack(fill = BOTH, expand = YES)
#frame.pack_propagate(False)
#Editing the app's background
img = ImageTk.PhotoImage(Image.open("background.png"))
background_label = Label(app, image = img)
background_label.place(x = 0, y = 0, relheight= 1, relwidth= 1)
#background_label.bind('<Configure>', resize_image)

collab_lbl = Label(app, text = "INPUTS", font = ('arial bold', 30), bg = 'white')
collab_lbl.place(relx = 0.48, rely = 0.3, anchor = CENTER)

manual_lbl = Label(app, text = "User Manual - AI-enabled CyberSecurity Hackathon", font = ('arial bold', 12))
manual_lbl.place(relx = 0.35, rely = 0.3, anchor = E)

step1_lbl = Label(app, text = "1. Input the name of the app you want to check, must end with the file format", font = ('arial',10), bg = 'white')
step2_lbl = Label(app, text = "2. Input the URL of a webpage you want to check, must start with HTTP", font = ('arial', 10), bg = 'white')
step3_lbl = Label(app, text = "3. Click on visit website if you still want to have a look at a flagged website", font = ('arial', 10), bg = 'white')
#step4_lbl = Label(app, text = "4. Once it's finished updating, you can click on Open New Slides \n to open the updated slides. This is different from your template", font = ('arial', 10), bg = 'white')
#step5_lbl = Label(app, text = "5. Click on Open Source Sheet to open the Excel spreadsheet \n if you want to double check on the data", font = ('arial', 10), bg = 'white')
note_lbl = Label(app, text = "Note: You have to decrypt your pptx before running the code", font = ('arial italic', 10), bg = 'white')

step1_lbl.place(relx = 0.38, rely = 0.4, anchor = E)
step2_lbl.place(relx = 0.357, rely = 0.45, anchor = E)
step3_lbl.place(relx = 0.368, rely = 0.5, anchor = E)
#step4_lbl.place(relx = 0.334, rely = 0.65, anchor = E)
#step5_lbl.place(relx = 0.324, rely = 0.73, anchor = E)
note_lbl.place(relx = 0.30, rely = 0.6, anchor = E)

#create a label widget for entries
excel = Label(app, text = "File's name", font = ('arial italic', 11), bg = 'white')
powerpoint = Label(app, text = "Input URL", font = ('arial italic', 11), bg = 'white')

excel.place(relx  = 0.7, rely = 0.45, anchor = CENTER)
powerpoint.place(relx = 0.7, rely = 0.55, anchor = CENTER)

#Data Entry - source input
source_text = StringVar
source_entry = Entry(app,width = 30, borderwidth = 5, textvariable= source_text)
source_entry.place(relx = 0.5, rely = 0.45, anchor = CENTER)
#source_entry.insert(0, "Path to your Excel sheets:")

#Data Entry - source slide input
slide_text = StringVar
slide_entry = Entry(app, textvariable = slide_text,width = 30, borderwidth= 5)
slide_entry.place(relx = 0.5, rely = 0.55, anchor = CENTER)
#slide_entry.insert(0, "Path to your PowerPoint template:")

#source_entry.grid(row = 4, column = 6, sticky = E, pady = 2)
#slide_entry.grid(row = 5, column = 6, sticky = E, pady = 2)

Execute_btn = Button(app, text = "Check Application", font = 'italic', width = 16, command = mal_app, fg = 'blue')
Execute_btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)

Open_btn = Button(app, text = "Check URL", font = 'italic', width = 16, command = CheckUrl, fg = 'blue')
Open_btn.place(relx = 0.7, rely = 0.7, anchor = CENTER)

Excel_btn = Button(app, text = "Visit Website", font = 'italic', width = 16, command = sourcesheet, fg = 'blue')
Excel_btn.place(relx = 0.9, rely =0.7, anchor = CENTER)

contact_lbl = Label(app, text = "Something went wrong? Contact us at", font = ('arial italic', 10))
contact_lbl.place(relx = 0.2, rely = 0.95, anchor = SE)
#contact_lbl.pack()

link = Label(app, text = "nhoang1001@gmail.com", font = ('arial italic', 10), fg = 'red')
link.place(relx = 0.313, rely = 0.95, anchor = SE)
# link.bind("<Button-1>", lambda e:
#           callback('https://mail.google.com/mail/?view=cm&source=mailto&to=[keven@edgered.com.au]'))

app.mainloop()
