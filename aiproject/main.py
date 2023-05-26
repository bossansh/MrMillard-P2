#############################################################################
# Name: Anshul Prabu #221, Chayan Manchanda, Brandon Le                     #
# Project: Password Generator												#
#                                                                           #
# Description: Uses chatGPT to either create a random strong password or    #
# make a common password stronger or make a password with certain           #
# requirements							                                    #
#############################################################################
import tkinter as tk
import random
import openai
import io
from PIL import Image, ImageTk


main = tk.Tk()


canvas = tk.Canvas(main, width=400, height=400)
canvas.grid(columnspan=5, rowspan=11) #splits canvas into three identical columns and seven rows so that the buttons and texts can be placed properly.

#logo
logo = Image.open('logo.png') #takes logo image and places at top of window
logo = logo.resize((200,200))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)

openai.api_key = "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" #allows us to access chatGPT


random_text = tk.StringVar() 
randomPassword = tk.Button(main, textvariable=random_text, command=lambda:generate_password(), font ="Papyrus", bg="white", fg="black", height=2, width=15)
random_text.set("Generate Random Password")
randomPassword.grid(column=2, row=1)


#instructions
instructions = tk.Label(main, text="Input a phrase in the box below to turn it into a strong password.", font="Papyrus")
instructions.grid(columnspan = 3, column=1, row=3) #places instructions for the strengthen password

strengthen_text_box = tk.Text(main, height=1, width=50, padx=15, pady=15) #styling for text box
strengthen_text_box.tag_configure("center", justify="center") #creates input for phrase to be strengthened
strengthen_text_box.tag_add("center", 1.0, "end")
strengthen_text_box.grid(column=2, row=4)

strengthen_text = tk.StringVar() #creates a button that runs the strengthen password function and takes the input from the text box as argument
strengthenPassword = tk.Button(main, textvariable=strengthen_text, command=lambda:strengthen_password(strengthen_text_box.get(1.0, "end-1c")), font ="Papyrus", bg="white", fg="black", height=2, width=15)
strengthen_text.set("Strengthen Password")
strengthenPassword.grid(column=2, row=5)
#instructions for custom password generation
custom_instructions = tk.Label(main, text="In the boxes below, type the number of each type of character you want in your password", font="Papyrus")
custom_instructions.grid(columnspan = 3, column=1, row=7) #places instructions for each of the five text boxes for the custom password
custom_instructions = tk.Label(main, text="# of characters", font="Papyrus") 
custom_instructions.grid(columnspan = 1, column=0, row=8) 
custom_instructions = tk.Label(main, text="# of uppercase", font="Papyrus")
custom_instructions.grid(columnspan = 1, column=1, row=8) 
custom_instructions = tk.Label(main, text="# of lowercase", font="Papyrus")
custom_instructions.grid(columnspan = 1, column=2, row=8) 
custom_instructions = tk.Label(main, text="# of numbers", font="Papyrus")
custom_instructions.grid(columnspan = 1, column=3, row=8) 
custom_instructions = tk.Label(main, text="# of specials", font="Papyrus")
custom_instructions.grid(columnspan = 1, column=4, row=8) 

#text box to input number of characters
character_text_box = tk.Text(main, height=1, width=10, padx=15, pady=15) #styling for text box
character_text_box.tag_configure("center", justify="center")
character_text_box.tag_add("center", 1.0, "end")
character_text_box.grid(column=0, row=9)

#text box to input number of uppercase letter
uppercase_text_box = tk.Text(main, height=1, width=10, padx=15, pady=15) #styling for text box
uppercase_text_box.tag_configure("center", justify="center")
uppercase_text_box.tag_add("center", 1.0, "end")
uppercase_text_box.grid(column=1, row=9)

#text box to input number of lowercase letters
lowercase_text_box = tk.Text(main, height=1, width=10, padx=15, pady=15) #styling for text box
lowercase_text_box.tag_configure("center", justify="center")
lowercase_text_box.tag_add("center", 1.0, "end")
lowercase_text_box.grid(column=2, row=9)

#text box to input number of numbers
numbers_text_box = tk.Text(main, height=1, width=10, padx=15, pady=15) #styling for text box
numbers_text_box.tag_configure("center", justify="center")
numbers_text_box.tag_add("center", 1.0, "end")
numbers_text_box.grid(column=3, row=9)

#text box to input number of special characters
specials_text_box = tk.Text(main, height=1, width=10, padx=15, pady=15) #styling for text box
specials_text_box.tag_configure("center", justify="center")
specials_text_box.tag_add("center", 1.0, "end")
specials_text_box.grid(column=4, row=9)

#creates button that runs the custom password button on press. Takes in the arguments of all the five text boxes to produce a result
custom_text = tk.StringVar() 
customPassword = tk.Button(main, textvariable=custom_text, command=lambda:custom_password(character_text_box.get(1.0, "end-1c"), uppercase_text_box.get(1.0, "end-1c"), lowercase_text_box.get(1.0, "end-1c"), numbers_text_box.get(1.0, "end-1c"), specials_text_box.get(1.0, "end-1c")), font ="Papyrus", bg="white", fg="black", height=2, width=15)
custom_text.set("Generate Custom Password")
customPassword.grid(column=2, row=10)



def generate_password():
    # Define the prompt that the API will use to generate the response
    prompt = f"Generate a strong password"
    
    # Define the parameters for the API request
    model_engine = "GPT-3"  # Choose the GPT-3 model engine
    temperature = random.uniform(0.5, 1)  # Choose a random temperature between 0.5 and 1
    max_tokens = 1024  # Set the maximum number of tokens to generate
    
    # Send a request to the GPT-3 API to generate the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Return the generated response
    #text box
    text_box = tk.Text(main, height=5, width=50, padx=15, pady=15) #text box style
    text_box.insert(1.0, response.choices[0].text)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=2, row=2)


def strengthen_password(phrase):
    # Define the prompt that the API will use to generate the response
    # Makes input from text box a strong password
    str1 = "Make "
    str2 = phrase
    str3 = " a strong password"
    prompt = str1 + str2 + str3
    
    # Define the parameters for the API request
    model_engine = "GPT-3"  # Choose the GPT-3 model engine
    temperature = random.uniform(0.5, 1)  # Choose a random temperature between 0.5 and 1
    max_tokens = 1024  # Set the maximum number of tokens to generate
    
    # Send a request to the GPT-3 API to generate the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    text_box = tk.Text(main, height=5, width=50, padx=15, pady=15) #text box style
    text_box.insert(1.0, response.choices[0].text)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=2, row=6)

def custom_password(characters, uppercase, lowercase, numbers, specials):
    # Define the prompt that the API will use to generate the response
    #Takes in all 5 arguments that the user inputted and creates the prompt.
    str1 = "Generate a password with "
    str2 = characters
    str3 = ", "
    str4 = uppercase
    str5 = " letters"
    str6 = lowercase
    str7 = numbers
    str8 = " numbers"
    str9 = "and "
    str10 = specials
    str11 = " special characters"
    str12 = " characters"
    str13 = " uppercase"
    str14 = " lowercase"
    prompt = str1 + str2 + str12 + str3 + str4 + str13 + str5 + str3 + str6 + str14 + str5 + str3 + str7 + str8 + str3 + str9 + str10 + str11
    
    # Define the parameters for the API request
    model_engine = "GPT-3"  # Choose the GPT-3 model engine
    temperature = random.uniform(0.5, 1)  # Choose a random temperature between 0.5 and 1
    max_tokens = 1024  # Set the maximum number of tokens to generate
    
    # Send a request to the GPT-3 API to generate the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Parse the response and extract the generated information
    #password = response.choices[0].text
    
    # Return the generated response
    text_box = tk.Text(main, height=5, width=50, padx=15, pady=15) #text box style
    text_box.insert(1.0, response.choices[0].text)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=2, row=11)

main.mainloop()
