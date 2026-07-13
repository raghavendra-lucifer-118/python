# Taking input sentence
sentence = input("Enter a sentence: ")
search_word = input("Enter Search Word: ")
replace_word = input("Enter replace Word: ")


# split to make words from a single str sentence
sentence_list = sentence.split(" ")

# First 5 and Last 5 characters
print("First 5:",sentence[:5])
print("Last 5:",sentence[-5:])

# To uppercase and To lowercase
print("Upper:",sentence.upper())
print("Lower:",sentence.lower())

# Number of words and presence of search word in sentence
print("Words:", len(sentence_list))
print("Yes" if search_word in sentence else "No")

#Replace and update the search word in sentence
sentence = sentence.replace(search_word , replace_word)
print("Updated:",sentence)
