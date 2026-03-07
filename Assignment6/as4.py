def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = input("Enter text: ")
result = word_frequency(text)

print("Word frequencies:")
for word, count in result.items():
    print(word, ":", count)