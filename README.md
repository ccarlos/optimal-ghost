optimal-ghost
=============
Usage: python ghost.py inputfile

Optimal Ghost

In the game of Ghost, two players take turns building up an English word from left to right. Each player adds one letter per turn. The goal is to not complete the spelling of a word: if you add a letter that completes a word (of 4+ letters), or if you add a letter that produces a string that cannot be extended into a word, you lose. (Bluffing plays and "challenges" may be ignored for the purpose of this puzzle.) 

Write a program that allows a user to play Ghost against the computer. 

The computer should play optimally given the following dictionary: WORD.LST (1.66 MB). Allow the human to play first. If the computer thinks it will win, it should play randomly among all its winning moves; if the computer thinks it will lose, it should play so as to extend the game as long as possible (choosing randomly among choices that force the maximal game length).

Resources:
WORD.LST
http://itasoftware.com/careers/work-at-ita/PuzzleFiles/WORD.LST

References:
http://vkedco.blogspot.com/2012/02/trie-in-python.html
http://pypi.python.org/pypi/trie
http://en.wikipedia.org/wiki/Trie
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=usingTries
