# The following script is a solution to http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
# ------------------------------------------------------------------
# Interactive Python Section 1.12 - Defining Functions  - Self Check

# You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

#You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

#A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.
# --------------------------------------------------------------------

import random
import string

ALLOWED_CHARS = string.ascii_lowercase + " "


def generate(n):
    return "".join(random.choice(ALLOWED_CHARS) for _ in range(n))
# ------------------------------------------------------------------------    
# Python has an official style-guide, PEP8, which programmers are encouraged to adhere to. It recommends using lower_case_with_underscores as variable and function names.

# Python also has a built-in module called string, which has all lowercase characters. With it, generating a random sentence becomes a lot easier. I renamed this function generate, to adhere more closely to the requirements. It uses random.choice, which just chooses a random element from a sequence and _ as a placeholder for the unused loop variable.

#-------------------------------------
# The scoring function below is implemented using sum and iterating over both sentences simultaneously:

def score(user_sentence, sentence):
    return sum(user_char == char for user_char, char in zip(user_sentence, sentence))
#---------------------------------

#Alternatively, you could use the Levenshtein distance as score:

#$ pip install python-Levenshtein

#Which you can then use like this:

#import Levenshtein

#def score(user_sentence, sentence):
#    return len(user_sentence) - Levenshtein.distance(user_sentence, sentence)

#When testing these two score functions, the Levenshtein seems to be about twice as fast:


#The actual main function can be a lot simpler, I use itertools.count to have a loop that runs infinitely long and keeps track of how many iterations it has gone through.
