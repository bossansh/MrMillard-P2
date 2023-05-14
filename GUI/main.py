#############################################################################
# Description: This GUI has a button which allows a user to select a text   #
# from their files, and this text will pop-up below. The text box allows    #
# user input. If the user wants to change something in the PDF, they can    #
# edit in the text box and then save it in a new one. I learned the tkinter #
# basics via W3 schools and took a lot of the functions from stack overflow #
#############################################################################

import tkinter as tk
import PyPDF2 
import io
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas


main = tk.Tk()

canvas = tk.Canvas(main, width=600, height=300)
canvas.grid(columnspan=3, rowspan=7) #splits canvas into three identical columns and seven rows so that the buttons and texts can be placed properly.

#logo
logo = Image.open('logo.png') #takes logo image and places at top of window
logo = logo.resize((300,200))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(main, text="Select a PDF file on your computer to extract its text. Once extracted click on the text box to edit the PDF.", font="Papyrus")
instructions.grid(columnspan = 3, column=0, row=1) #places instructions in just below logo

def open_file(): #opens user's files, and asks to select one to be placed into window
    browse_text.set("loading... ")
    file = askopenfile(parent=main, mode="rb", title="choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        reader = PyPDF2.PdfReader(file) #takes file to read and extract text
        page = reader.pages[0]
        page_content = page.extract_text()
        #text box
        text_box = tk.Text(main, height=10, width=50, padx=15, pady=15) #styling for text box
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        #save button
        global save_text
        save_text = tk.StringVar() #runs save_edit (lines 60-75) on button press.
        save_btn = tk.Button(main, textvariable=save_text, command=lambda:save_edit(), font ="Papyrus", bg="white", fg="black", height=2, width=15)
        save_text.set("Save As") 
        save_btn.grid(column=1, row=4)
        

        browse_text.set("Browse")
    def save_edit():
        save_text.set("Save as")
        PDFname = tk.Text(main, height=1, width=50, padx=15, pady=15) #styling for text box
        PDFname.tag_configure("center", justify="center") #user's input in this text box will be name of pdf file edited text will be saved in
        PDFname.tag_add("center", 1.0, "end")
        PDFname.grid(column=1, row=6)

        #PDF name instructions
        username = tk.Label(main, text="Insert name of the new PDF (.pdf at end). Click save to save as new file. ", font="Papyrus")
        username.grid(columnspan = 3, column=0, row=5) #places instructions above the new text box created

        global add_text #creates save button to add the pdf into the folder
        add_text = tk.StringVar() #runs addPDF (lines 76-83) on button press.
        add_btn = tk.Button(main, textvariable=add_text, command=lambda:addPDF(), font ="Papyrus", bg="white", fg="black", height=2, width=15)
        add_text.set("Save")
        add_btn.grid(column=1, row=7)
        def addPDF():
            text = text_box.get(1.0, "end-1c") #makes text in text box a string
            usertext = PDFname.get(1.0, "end-1c") #makes user's text for pdf name a string
            canvas = Canvas(usertext) #makes pdf with name inserted in table
            canvas.drawString(72, 72, text) #adds text to that pdf
            canvas.save()

            save_text.set("Save as")
        

        

#browse button
browse_text = tk.StringVar() #runs open_file (lines 38-59)on button press.
browse_btn = tk.Button(main, textvariable=browse_text, command=lambda:open_file(), font ="Papyrus", bg="white", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)





canvas = tk.Canvas(main, width=600, height=250)
canvas.grid(columnspan=3)



main.mainloop()
