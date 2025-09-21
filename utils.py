import json
import string
import sys

"""
Read 'emoji.json' file
"""
def load_emoji(file_path='data/emoji.json'):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data
    
"""
Lower case and remove punctuation.
"""
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation)).strip()
    return text

"""
Find emoji in the text, return default if none.
"""
def find_emoji(text, emoji_dict):
    text = clean_text(text)

    matched_emojis = []

    for emoji in emoji_dict:
        if emoji in text:
            matched_emojis.append(emoji_dict[emoji])        

    if matched_emojis:
        return ", ".join(matched_emojis)
    else:
        return emoji_dict['default']

"""
Exit if the user enters 'exit' or 'quit'
"""
def exit_sys(user_input):
    if user_input.lower() in ('exit', 'quit'):
        print("Thanks!")
        sys.exit()


