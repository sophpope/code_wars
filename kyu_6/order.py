# Your order please 6kyu

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence: str) -> str:
    list_sentence =  sentence.split(" ")
    sorted_sentence = sorted(list_sentence, key=lambda word: [int(char) for char in word if char.isdigit()])
    return " ".join(sorted_sentence)

print(order("is2 Thi1s T4est 3a"))