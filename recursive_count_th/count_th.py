'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
"""
# This passes all tests and isn't recursive
def count_th(word):
    # TBC
    print(word.count("th"))
    return word.count("th")
"""

def count_th(word, i=0, count=0):
    length = len(word) - 1
    if i < length:
        if word[i] + word[i+1] == "th":
            count += 1
            return count_th(word, i + 1, count)
        else:
            return count_th(word, i + 1, count)
    print(word, count)
    return count
