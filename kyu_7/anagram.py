def is_anagram(test, original):
    lower_test = test.lower()
    lower_original = original.lower()
    sorted_test = ''.join(sorted(lower_test))
    sorted_org = ''.join(sorted(lower_original))
    if sorted_test == sorted_org:
        return True, f'The word {test} is an anagram of {original}'
    else:
        return False 
    
print(is_anagram('Buckethead', 'DeathCubeK'))

