# pig-latin-translator-python

This Python program uses the `tkinter` library to create a graphical user interface (GUI) for a Pig Latin translator. The user can enter some text in an input field, and then click a button to translate the text to Pig Latin. The translated text is displayed in an output field.

## Running the Program

To run the program, open a terminal and navigate to the directory containing the `pig_latin_translator.py` file. Then run the following command:
```
python pig_latin_translator.py
```

This will open the Pig Latin translator GUI window.

## Using the Program

1. Enter some text in the input field.
2. Click the "Translate" button.
3. The translated text will be displayed in the output field.

## Implementation Details

The `to_pig_latin` function is responsible for translating a string of text to Pig Latin. It does this by first splitting the text into a list of words, and then translating each word to Pig Latin using a helper function called `translate_word`. The `translate_word` function handles the translation of a single word by moving its initial consonant or consonant cluster to the end of the word and adding "ay" to the end.

The `translate` function is called when the user clicks the "Translate" button. It gets the text from the input field, translates it to Pig Latin using the `to_pig_latin` function, and displays the result in the output field.
