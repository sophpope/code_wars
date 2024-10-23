# Human Readable Time 5kyu

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

# from datetime import timedelta
# def make_readable(time):
#     return timedelta(seconds = time)


import time
def make_readable(seconds):
    if seconds > 359999:
        return False
    else:
        convert = time.strftime('%H:%M:%S', time.gmtime(seconds))
        return convert


print(make_readable(60))