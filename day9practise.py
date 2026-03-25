#Simple Text Utility Tool

text = input("Enter a sentence: ")
#1. Word count
words = text.split()
print("Word count:", len(words))

#2. Reverse text
print("Reversed:", text[::-1])

#3. Palindrome check
clean = text.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

#4. Most frequent word
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)
print("Most frequent word:", max_word)

#5. Remove duplicate words
unique = list(dict.fromkeys(words))
print("Without duplicates:", " ".join(unique))
