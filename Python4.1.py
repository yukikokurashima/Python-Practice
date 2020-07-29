string=input("Please enter a sentence:\t")
strlist=string.split()
pig_latin=''
for word in strlist:
    word=word[1:]+word[0]+'ay '
    pig_latin+=word
print("Pig Latin of the sentence is:",pig_latin)