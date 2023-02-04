#############################################################################
# Name: Anshul Prabu #221                                                   #
# Project: First GUI 													    #
#                                                                           #
# Description: This GUI has a button which allows a user to select a text   #
# from their files, and this text will pop-up below							#
#############################################################################

import tkinter as tk
import PyPDF2 
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

main = tk.Tk()

canvas = tk.Canvas(main, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3) #splits canvas into three identical columns for precision

#logo
logo = Image.open('logo.png') #takes logo image and places it in window
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(main, text="Select a PDF file on your computer to extract its text", font="Papyrus")
instructions.grid(columnspan = 3, column=0, row=1) #places instructions in certain part of window

def open_file(): #opens user's files, and asks to select one to be placed into window
    browse_text.set("loading... ")
    file = askopenfile(parent=main, mode="rb", title="choose a file", filetype=[("Pdf file", "*.pdf")]) #filetypes for mac
    if file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        page_content = page.extract_text()
        #text box
        text_box = tk.Text(main, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar() #runs open_file on button press.
browse_btn = tk.Button(main, textvariable=browse_text, command=lambda:open_file(), font ="Papyrus", bg="#69420a", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(main, width=600, height=250)
canvas.grid(columnspan=3)



main.mainloop()
