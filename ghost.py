from random import choice
from string import ascii_lowercase
from sys import argv, exit, stderr
from time import sleep

from trie import Trie


class OptimalGhost:
    def __init__(self):
        self.tr = Trie()

    # NOTE: Assumes file_name has one word per line as found in WORD.LST.
    def load_words(self, file_name):
        """Load Trie data structure with words of len >= 4."""

        ins_key = self.tr.insert_key
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) >= 4:
                    ins_key(line, True)

    def computer_letter_choice(self, curr_word, turn):
        """Optimally choose the next letter in the game.

        At the current game state we will keep track of the possible
        letter choices to advance using Trie.start_with_prefix. Our initial
        choice is to choose a letter in a word(odd length) that will increase
        our chances of winning, otherwise we will choose a word(even length)
        with maximal length to keep the game going.
        """

        print "Computer's Turn ->"
        sleep(1.0)
        win_wrds = self.tr.start_with_prefix(curr_word)
        odd_wrds = [w for w in win_wrds if len(w) % 2 == 1]
        evn_wrds = [w for w in win_wrds if len(w) % 2 == 0]
        evn_wrds.sort(key=len, reverse=True)

        word = ''
        if odd_wrds:
            word = choice(odd_wrds)
            if len(word) == turn + 1:
                word = choice(odd_wrds)
        elif evn_wrds:
            word = evn_wrds[0]
        else:
            word = choice(ascii_lowercase)

        next_letter = word[turn] if len(word) > 1 else word[0]

        return next_letter

    def boot_game(self):
        """Start an interactive game of Optimal Ghost.

        A real player starts first and afterwards it is the computer's
        turn. After either entity has entered a choice we will check whether
        they have completed a word or if they have entered a letter that
        doesn't allow to advance a game.
        """

        player_turn = 'Player'
        curr_word = ''
        turn = 0
        print "\nWelcome to Optimal Ghost!\n"

        while(True):
            print 'Current Word: {0}'.format(curr_word)

            if player_turn == 'Player':
                next_letter = raw_input("Enter a letter -> ").strip()
                if next_letter not in ascii_lowercase:
                    print "Please enter a lower case letter."
                    continue
                elif len(next_letter) != 1:
                    print "Please enter a single letter."
                    continue
                curr_word = curr_word + next_letter
            else:  # Computer turn
                next_letter = self.computer_letter_choice(curr_word, turn)
                print 'Computer chooses letter: {0}'.format(next_letter)
                curr_word = curr_word + next_letter

            # check valid word
            if self.tr.tr_has_key(curr_word):
                print '*** {0} Loses ***'.format(player_turn)
                print '*** Completed word: {0}'.format(curr_word)
                break

            # check invalid word + cannot advance, eg allx
            if not self.tr.start_with_prefix(curr_word):
                print '*** {0} Loses ***'.format(player_turn)
                print '*** Invalid word, cannot advance: {0}'.format(curr_word)
                break

            turn = turn + 1
            player_turn = 'Computer' if player_turn == 'Player' else 'Player'


def main(argv):
    """
    Usage: python ghost.py inputfile

    See README for problem description.

    main() will read in lines from inputfile. Valid lines will be parsed and
    update the current object. After initialization boot_game() will be called
    and launch a game of optimal ghost.
    """

    if len(argv) != 1:
        print >> stderr, "Insufficient number of arguments."
        print >> stderr, "Usage: ghost.py filename"
        exit(2)

    file_name = argv[0]

    opt = OptimalGhost()
    opt.load_words(file_name)

    while True:
        opt.boot_game()
        q = raw_input("Would you like to quit? [Y|y or N|n]:").strip()
        if q == 'Y' or q == 'y':
            break
        elif q == 'N' or q == 'n':
            continue
        else:
            print 'Invalid input: You must play again with the ghost'


if __name__ == '__main__':
    exit(main(argv[1:]))
