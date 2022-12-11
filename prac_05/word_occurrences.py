user_text = []
text = input("Text: ")
user_text.append(text)
word_to_count = {}
for line in user_text:
    words = line.split(" ")
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
width = 13
for keys in sorted(word_to_count):
    print(f"{keys:{width}} : {word_to_count[keys]}")