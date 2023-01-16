# Word Ladder Solver

This is a short script that finds the shortest path from one word to another by changing only one character at a time, a challenge known as a word ladder. Party inspired by wordle and finding connections between words and having seen and done these puzzles in puzzle books years ago.

Made early spring 2022.

## Use

The `WordLadder.py` file is a standalone script. Run the file and input any two valid scrabble words (lowercase) separated by a space. The script will show the depth first search algorithm at work by showing the currently examined word in addition to how many letters apart it is from the final word.

Note: Because the algorithm performs a DFS, it may find a solution quicker if the word orders are swapped. This is a difference that could be reduced dramatically if a Breadth first search (BFS) were employed.

## Optimizations

-  Since word ladders can be only found between word pairs of the same length, the `LengthDicts` folder contains the all valid scrabble words split by their length. The algorithm only considers a single file containing all valid words of the same length, and ignores unecessary searches.
- The algorithm also searches for any word that is one letter away from the target word, because once such a word is found, it is always possible to change an additional letter to make it the target word.
- The algorithm will also ignore subtrees where the root of such a subtree is a word that has already been the root of a previously searched tree. This removes infinitely regressive searches from the algorithm.

## Examples

Listed below are good examples of word pairs to see the algorithm in action. Word pairs are from the `Good WL Examples.txt` file.

`fail mate`
`crane state`
`paper holds`
`cord bean`
`pause cases`
`chair files`
`ladder hammer`
`chart frame`
`notes block`
`masks break`
`trucker kitchen`
`chairs summer`
`quilt tower`
`hammer tokens`
`harden clicks`
`phone apple`
`henry david`
`great value`
