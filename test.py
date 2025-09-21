from utils import load_emoji, clean_text, find_emoji

def run_tests():
    # Load emoji dictionary
    emoji_dict = load_emoji("data/emoji.json")

    # --- clean_text tests ---
    assert clean_text("Hello!!!") == "hello"
    assert clean_text("I'm HAPPY.") == "im happy"
    assert clean_text("  Sad?  ") == "sad"

    # --- find_emoji tests ---
    assert find_emoji("I am happy", emoji_dict) == "😃"
    assert find_emoji("Feeling sad today", emoji_dict) == "😢"
    assert find_emoji("I am angry", emoji_dict) == "😡"
    assert find_emoji("This is random text", emoji_dict) == emoji_dict.get("default", "🤔")

    print("✅ All tests passed!")

if __name__ == "__main__":
    run_tests()
