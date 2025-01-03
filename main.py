from collections import Counter

def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    character_counts = Counter(text)
    return dict(character_counts)

def main():
    with open("/home/zakarias/workspace/github.com/ZakariasFagerstedt/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print("There are ", count_words(file_contents) , " words in this book!")
    print(count_characters(file_contents))
if __name__ == "__main__":
    main()

