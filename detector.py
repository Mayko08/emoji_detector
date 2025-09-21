from utils import load_emoji, clean_text, find_emoji, exit_sys

def main():
    emoji_dict = load_emoji()
    
    while True:
        user = input("Sentence: ")
        user = clean_text(user)
        print()
        
        # Check if user wants to quit
        exit_sys(user)

        if user:
            result = find_emoji(user, emoji_dict)
            print("Found emojis:", result)
        else:
            print("You haven't typed anything yet.")
        
        print()
        
if __name__ == "__main__":
    main()
