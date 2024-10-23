def likes(names):
    count = len(names)
    extra = count - 2
    if count < 1:
        return "no one likes this"
    elif count == 1:
        return f'{names[0]} likes this'
    elif count == 2:
        return f'{names[0]} and {names[1]} likes this'
    elif count == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif count >= 4:
        return f'{names[0]}, {names[1]} and {extra} others like this'
    


print(likes(["Max", "John", "Mark"]))