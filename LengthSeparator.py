#
#
# This script is just to separate the words into different files
# By length, search through less
#
# SUCCESS!!
#
# Maverick Reynolds
# 03-08-2022
#
#

for i in range(20):
    
    with open('ScrabbleDictionary.txt') as all_words:
        for line in all_words:

            if len(line) == i + 1:
                with open(f'LengthDicts/sd{i}.txt', 'a') as curr:
                    curr.write(line)
