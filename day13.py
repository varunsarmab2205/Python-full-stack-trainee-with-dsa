,paragraph = "Varun Kandukuri is passionate about technology and learning Python."

vowels = ['a','e','i','o','u','A','E','I','O','U']

vowels_count = 0
consonents_count = 0

for i in paragraph:
    if i in vowels:
        vowels_count = vowels_count + 1
    elif i != " " and i != ".":
        consonents_count = consonents_count + 1

spaces_count = paragraph.count(" ")

print("Vowels:", vowels_count)
print("Consonents:", consonents_count)
print("Spaces:", spaces_count)
