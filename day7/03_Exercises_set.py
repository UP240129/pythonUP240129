age = [22, 19, 24, 25, 26, 24, 25, 24]
#Exercise 1 (Level 3)
age_set = set(age)
print(type(age_set))

if (len(age)>len(age_set)):
    print('La lista tiene más elementos')
elif(len(age)<len(age_set)):
    print('El set tiene mas elementos')
else:
    print('tienen la misma cantidad de elementos')

#Exercise 2 (Level 3)

#Exercise 3 (Level 3)
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace(".", "").split() 
unique_words= set(words)
print('Unique words:',unique_words)