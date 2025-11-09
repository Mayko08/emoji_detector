# Emoji Detector 😃🎉

## Description
The **Emoji Detector** is a simple Python tool that detects emotions or concepts in text and maps them to corresponding **emojis**.  
It uses a **JSON file** (`emojis.json`) for storing keyword-to-emoji mappings, making the system **easy to extend** and maintain.  

This project demonstrates **basic NLP preprocessing (text cleaning)**, **dictionary lookups**, and **data-driven design** — perfect for beginners in Python projects.

---

## Features
- Cleans text (lowercasing + removing punctuation)  
- Detects emojis from a dictionary of keywords  
- Supports multiple emoji matches in one sentence  
- Default emoji (`🤔`) when no match is found  
- Exit system with `exit` or `quit` commands  
- Modular design (helpers in `utils.py`)  

---

## File Structure
- `detector.py` → Main program (interactive loop for detecting emojis)  
- `utils.py` → Helper functions: load emoji data, clean text, find emojis, exit system  
- `test.py` → Simple tests for `utils.py` using `assert`  
- `data/`
  - `emojis.json` → Dictionary of keywords mapped to emojis  
- `README.md` → Project documentation 

## Example Interaction
Sentence: I am happy but tired

Found emojis: 😃, 😴

Sentence: I feel nothing

Found emojis: 🤔

Sentence: quit
Thanks!

## Technologies Used
- **Python 3**  
- **JSON** for keyword-to-emoji mapping  
- **String processing** for text cleaning  
- **Assert-based tests** for validation  

---

## Author
**Mayko**  
[GitHub Profile](https://github.com/Mayko08)  
AI and Python Enthusiast | High School Student | Aspiring Computer Scientist
