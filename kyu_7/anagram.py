def is_anagram(test, original):
    # make the input all lower case, so when sorted they will match
    lower_test = test.lower()
    lower_original = original.lower()
    # sort the letter, so if the words are anagrams they will match
    sorted_test = ''.join(sorted(lower_test))
    sorted_org = ''.join(sorted(lower_original))
    if sorted_test == sorted_org:
        return True
    else:
        return False 
    
print(is_anagram('Twoo', 'Woot'))

