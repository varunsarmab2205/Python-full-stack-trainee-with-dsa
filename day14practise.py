print(" Palindrome Checker ")

words = ["tenet", "madam", "hello", "level", "world"]

for word in words:
    rev = ""
    
    #reverse using for loop
    for j in word:
        rev = j + rev
    
    print("Word:", word)
    print("Reversed:", rev)
    
    if rev == word:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
    
    print("----")
