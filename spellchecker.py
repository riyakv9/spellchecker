from tkinter import Tk, Label, Text, Button, Scrollbar, END, messagebox
from spellchecker import SpellChecker

# Initialize SpellChecker
spell = SpellChecker()

# Function to check spelling
def check_spelling():
    text = input_text.get("1.0", END).strip()  # Get text from the input box
    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    misspelled_words = spell.unknown(text.split())
    
    if not misspelled_words:
        result_text.delete("1.0", END)
        result_text.insert(END, "No spelling errors found!")
    else:
        corrections = {}
        for word in misspelled_words:
            corrections[word] = spell.correction(word)
        
        result_text.delete("1.0", END)
        result_text.insert(END, "Misspelled Words and Suggestions:\n\n")
        for word, correction in corrections.items():
            result_text.insert(END, f"'{word}' -> '{correction}'\n")

# Function to clear input and output
def clear_text():
    input_text.delete("1.0", END)
    result_text.delete("1.0", END)

# Initialize Tkinter App
app = Tk()
app.title("Spell Checker App")
app.geometry("600x400")
app.resizable(False, False)

# Input Label and Text Area
Label(app, text="Enter Text to Check:", font=("Arial", 14)).pack(pady=10)
input_text = Text(app, height=8, width=70, wrap="word", font=("Arial", 12))
input_text.pack(pady=10)

# Scrollbar for Input Text Area
scrollbar = Scrollbar(app, command=input_text.yview)
scrollbar.pack(side="right", fill="y")
input_text.config(yscrollcommand=scrollbar.set)

# Buttons
Button(app, text="Check Spelling", font=("Arial", 12), command=check_spelling, bg="#007BFF", fg="white").pack(pady=10)
Button(app, text="Clear", font=("Arial", 12), command=clear_text, bg="#FF5733", fg="white").pack(pady=5)

# Result Label and Text Area
Label(app, text="Spelling Suggestions:", font=("Arial", 14)).pack(pady=10)
result_text = Text(app, height=8, width=70, wrap="word", font=("Arial", 12), state="normal")
result_text.pack(pady=10)

# Start the Tkinter Event Loop
app.mainloop()
