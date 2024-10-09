import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to handle user input and provide responses
def respond():
    user_input = entry.get()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: ", "bold")
        chat_log.insert(tk.END, user_input + "\n")
        chat_log.insert(tk.END, "Bot: ", "bold")
        chat_log.insert(tk.END, generate_response(user_input) + "\n\n")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a message!")

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()
    
    if "depressed" in user_input or "sad" in user_input:
        return "I’m really sorry you’re feeling this way. I’m here for you."
    elif "help" in user_input:
        return "I'm here to help you. Want to hear a joke to lighten things up?"
    elif "suicidal" in user_input or "suicide" in user_input:
        return "I'm really worried about you. Please talk to someone who can help. You matter!"
    elif "lonely" in user_input:
        return "You’re not alone. I’m here to keep you company."
    elif "loser" in user_input:
        return "You’re not a loser. Everyone has value, including you."
    elif "hopeless" in user_input:
        return "Even when it’s dark, there’s always a star in the sky. Let’s find it together!"
    elif "no friends" in user_input:
        return "Well, you’ve got one right here! How about a virtual high-five?"
    elif "hate" in user_input:
        return "Not true! I think you’re pretty awesome."
    elif "worthy" in user_input:
        return "Absolutely, you’re worthy. Your life matters."
    elif "always" in user_input:
        return "I’ll be here whenever you need to talk. I’m like peanut butter to your jelly."
    elif "listener" in user_input:
        return "Thanks! I try my best."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You’re welcome! Here’s a virtual hug."
    elif "later" in user_input:
        return "Cool! I’ll be right here, like a favorite playlist."
    elif "goodbye" in user_input or "bye" in user_input:
        return "Take care, and remember I’m here if you need anything."
    elif "yes" in user_input or "yeah" in user_input or "okay" in user_input or "great" in user_input or "sure" in user_input or "alright" in user_input or "cool" in user_input or "fine" in user_input or "got it" in user_input:
        responses = [
            "Yes? Awesome! Why don’t skeletons fight each other? They don’t have the guts!",
            "Cool! What do you call fake spaghetti? An impasta!",
            "Alright! Why don’t eggs tell jokes? They’d crack each other up!",
            "Sure thing! What do you get if you cross a snowman and a vampire? Frostbite!",
            "Great! What did one ocean say to the other ocean? Nothing, they just waved!"
        ]
        return random.choice(responses)
    else:
        return "I'm here to listen. Feel free to share more with me."

# Setting up the main window
root = tk.Tk()
root.title("CommuniMate - Mental Health Chatbot")
root.geometry("500x700")
root.configure(bg="white") 

# Adding the logo
img = Image.open("G:\CodSoft\CommuniMate\system.png")
img = img.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
logo_label = tk.Label(root, image=photo)
logo_label.pack(pady=5)

# Adding the motto
motto_label = tk.Label(root, text="We Care. We Listen.",font=("Helvetica", 8, "italic", "bold"), fg="black")
motto_label.pack(pady=5)

# Adding the chat log (Text box for displaying conversation)
chat_log = tk.Text(root, state=tk.DISABLED, width=55, height=25, bg="#b3ffff", font=("Arial", 10))
chat_log.pack(pady=5)
chat_log.tag_configure("bold", font=("Arial", 10, "bold"))
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Bot: ", "bold")
chat_log.insert(tk.END, "Hey there! How can I help?\n\n")
chat_log.config(state=tk.DISABLED)

# Adding the entry box for user input
entry = tk.Entry(root, width=40, font=("Arial", 10), bg="#99ddff", fg="black")
entry.pack(pady=10)

# Adding the Send button
send_button = tk.Button(root, text="Send", command=respond, width=10, font=("Arial", 12), bg="#006699", fg="white")
send_button.pack(pady=10)

# Running the application
root.mainloop()
