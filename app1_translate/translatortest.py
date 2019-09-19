import json
data = json.load(open("data.json"))

def translate(word):
    return data[word]

while True:
    print("\n\nType \"end\" to end")
    word = input("Enter a word to translate: ")
    if word == "end":
        print("Bye...\n\n")
        break
    else:
        print("\n\n" + word + ": ")
        print(translate(word))