# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# code without punctuation ignored
# def pig_it(text):  
#     word = text.split(" ")
#     pig = [words[1:] + words[0] + 'ay' for words in word]
#     sentence = " ".join(pig)
#     return sentence


    # ay = sentence.split(" ")
    # listed_result = [items[1:] +  for items in ay]
    # result = " ".join(listed_result)
    
import string 
def pig_it(text): 
    words = text.split(" ")
    pig = []
    for word in words:
        if word[-1] in string.punctuation:
            pig.append(word)
        else: pig.append(word[1:] + word[0] + 'ay')
    sentence = " ".join(pig)
    return sentence


print(pig_it('Pig latin is cool !'))