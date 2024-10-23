def find_it(seq):
    dict = {}
    for item in seq:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    count = list(dict.values())[0]
    for ele in dict:
        if dict[ele] % 2 != 0:
            return ele