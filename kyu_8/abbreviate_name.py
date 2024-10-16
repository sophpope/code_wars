# Abbreviate a two word name 8 kyu

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    # Split name into a list
    name_split = name.split(" ")
    # Iterate through list to get first character
    initials = [word[0] for word in name_split]
    # Join first initials with a '.' and make sure it is upper case
    joined_initials = ".".join(initials).upper()
    return joined_initials
     

print(abbrev_name('Sophie Pope'))