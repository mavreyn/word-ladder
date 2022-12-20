# Word Ladder Solver

Short script that finds the shortest path from one word to another by changing only one character at a time, a challenge known as a word ladder.

## Use

The `WordLadder.py` file is a standalone script. Run the file and input any two valid scrabble words (lowercase) separated by a space. The script will show the depth first search algorithm at work by showing the currently examined word in addition to how many letters apart it is from the final word

Note: Because the algorithm performs a DFS, it may find a solution quicker if the word orders are swapped. This is a difference that could be reduced dramatically if a Breadth first search (BFS) were employed
