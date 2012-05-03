from string import ascii_lowercase
from sys import argv, exit, stderr

from trie import Trie


class OptimalGhost:
    def __init__(self):
        self.tr = Trie()

    # NOTE: Assumes file_name has one word per line as found in WORD.LST.
    def load_words(self, file_name):
        ins_key = self.tr.insert_key
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) >= 4:
                    ins_key(line, True)

    def boot_game(self):
        player_turn = 'me'
        curr_word = ''
        print "Welcome to Optimal Ghost!"

        while(True):
            print 'Current Word: {0}'.format(curr_word)

            if player_turn == 'me':
                next_letter = raw_input("Enter a letter: ").strip()
                if next_letter not in ascii_lowercase:
                    print "Please enter a lower case letter."
                    continue
                elif len(next_letter) != 1:
                    print "Please enter a single letter."
                    continue
                curr_word = curr_word + next_letter
            else:
                # TODO: Input AI functionality.
                print "comp turn::"

            #check valid word
            if self.tr.tr_has_key(curr_word):
                print '{0} Loses:'.format(player_turn)
                break

            #TODO: check invalid word + cannot advance, eg allx
            #if set is empty() of children of possible next words

            player_turn = 'comp' if player_turn == 'me' else 'me'


def main(argv):
    """
    Usage: python ghost.py inputfile

    See README for problem description.

    main() will read in lines from inputfile. Valid lines will be parsed and
    update the current object.
    """
    if len(argv) != 1:
        print >> stderr, "Insufficient number of arguments."
        print >> stderr, "Usage: ghost.py filename"
        exit(2)

    file_name = argv[0]
    opt = OptimalGhost()

    opt.load_words(file_name)

    #TODO: implement a way to let players keep playing.
    opt.boot_game()


if __name__ == '__main__':
    exit(main(argv[1:]))
