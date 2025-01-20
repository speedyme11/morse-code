"""Imports"""
import json


user_input = input("Enter some text to be converted to Morse Code: ")
class Converter:
    """Class to handle conversion"""

    def __init__(self, phrase):
        self.phrase = phrase.upper().strip()

    def converting(self) -> list:
        characters = []
        for i, letters in enumerate(self.phrase):
            characters.append(letters)
        return characters
    
    def morse_code(self) -> str:
        letters = self.converting()
        morse_code = []

        with open(file="morse-code.json", mode="r", encoding="utf-8") as morse:
            code = json.load(morse)

        for codes in letters:
            morse_code.append(code[codes])
        converted = " ".join(morse_code)
        return converted

convert = Converter(user_input)
print(convert.morse_code())
