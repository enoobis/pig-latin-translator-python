import tkinter as tk

def to_pig_latin(text):
    def translate_word(word):
        if word[0] in "aeiouAEIOU":
            return word + "ay"
        else:
            return word[1:] + word[0] + "ay"
    
    # Split the text into a list of words
    words = text.split()
    
    # Translate each word to Pig Latin
    pig_latin_words = [translate_word(word) for word in words]
    
    # Join the translated words back into a single string
    return " ".join(pig_latin_words)

def translate():
    # Get the text from the input field
    text = input_field.get()
    
    # Translate the text to Pig Latin
    pig_latin = to_pig_latin(text)
    
    # Display the translated text in the output field
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, pig_latin)
    output_field.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Pig Latin Translator")

# Set the background color to dark grey
window.config(bg="#222222")

# Create the input field
input_field = tk.Entry(window, width=50, bg="#444444", fg="#ffffff")
input_field.pack()

# Create the translate button
translate_button = tk.Button(window, text="Translate", command=translate, bg="#444444", fg="#ffffff")
translate_button.pack()

# Create the output field
output_field = tk.Text(window, width=50, height=10, state="disabled", bg="#444444", fg="#ffffff")
output_field.pack()

# Run the main loop
window.mainloop()