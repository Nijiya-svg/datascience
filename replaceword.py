
search_word = input("Enter the word to search: ")
replace_word = input("Enter the word to replace it with: ")


file = open("old.txt", "r")
content = file.read()
file.close()


content = content.replace(search_word, replace_word)


file = open("new.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully in 'new.txt'")
