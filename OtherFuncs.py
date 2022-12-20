#
# Other Stuff for fun, functions to find info
# 02-13-2022
# Superbowl Sunday
#
#


def longest_word():
    with open('ScrabbleDictionary.txt') as all_words:
        words = []
        desired = []

        for line in all_words:
            word = line[:-1]
            words.append(word)
        
        desired = [len(word) for word in words]

    return words[desired.index(max(desired))]

input(longest_word())
