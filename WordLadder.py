#
#
# This is gonna be fun
# I want to make something that transforms a word into another word
# One letter at a time
# Or changes the size by one character
# A word ladder
#
# Maverick Reynolds
# 02-09-2022 - 04-23-2022
#
#
#       FUNCTION VERSIONS:
#           - 1.0.0     Brute force
#
#           - 1.1.0     Sort list based on distance
#           - 1.1.1     Dist 1 means guaranteed solution
#           - 1.1.2     Dist less than one: 0 or 1
#
#           - 1.2.0     Skips prev attmpted words in tree
#           - 1.2.1     Need depth at least difference
#
#           - 2.0.0     Performs IDDFS
#           - 2.0.1     Only reads from file once
#
#


import sys
import time

# Global variable
attempted_words = []

# Benchmark function to check improvements
def bench():
    global attempted_words
    attempted_words = []

    start_time = time.perf_counter()
    is_word_present('CHAIR', 'FILES', 10, get_words(5))
    end_time = time.perf_counter()

    print(end_time - start_time)

# Doesn't work in command prompt
def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

# Char distance between words
def compare(a,b):   
    return sum(l != m for l, m in zip(a, b))

# Checks if the last n entries of list are the same
def same_last_entries(l,n):
    return l[-n:] == [l[-1]]*n

# Gets words of length, reads file once
def get_words(l):
    with open('ScrabbleDictionary.txt') as f:
        return [w for w in f.read().splitlines() if len(w) == l]

# Gets words one character apart from parameter
def words_one_apart(lst, wrd):
    return [w for w in lst if compare(w, wrd) == 1]

# Finds if the word is present in a tree of given depth
def is_word_present(bgn, fnsh, dpth, wrd_lst):
    curr_dist = compare(bgn, fnsh)

    # Base cases
    if curr_dist <= 1:
        return True
    elif dpth + 1 < curr_dist or bgn in attempted_words:
        delete_last_line()
        return False
    else:
        # Recursive call
        attempted_words.append(bgn)

        options = words_one_apart(wrd_lst, bgn)
        dists = [compare(wrd, fnsh) for wrd in options]
        ordered_wd_pairs = sorted(zip(dists, options))

        for dist, cand in ordered_wd_pairs:
            print(cand, dist)

            if is_word_present(cand, fnsh, dpth-1, wrd_lst):
                return True
    
        delete_last_line()
        return False


def main():
    global attempted_words

    LIMIT = 3
    MAX_DEPTH = 20

    while True:
        is_present = False

        # Gather information
        w1, w2 = input('> ').upper().split()
        distance = compare(w1, w2)
        all_words = get_words(len(w1))
        depth = distance
        awls = [0]

        # If it can still search and has not been getting stagnant results
        while not is_present and depth <= MAX_DEPTH and not same_last_entries(awls, LIMIT):
            attempted_words = []

            # Run search
            print(w1, distance)
            is_present = is_word_present(w1, w2, depth, all_words)          

            awls.append(len(attempted_words))
            depth += 1

        # When loop breaks
        if is_present:
            print(w2, '0')
        else:
            print(False)


if __name__ == '__main__':
    main()


