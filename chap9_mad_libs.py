from random import choice as choose
from random import seed

seed()
# lists of words to use (will be randomized)
animal = ['panda', 'bear', 'python', 'dog', 'roach']
action = ['walked', 'jumped', 'ran', 'flew', 'swam']

# create text string with sample words
# "The ADJECTIVE [animal] [past tense action] to the NOUN and then VERB.
# A nearby NOUN was unaffected by these events."
string = f'The ADJECTIVE {choose(animal)} {choose(action)} to the NOUN and ' \
         'then VERB. A nearby NOUN was unaffected by these events.\n'

# save string into a file
fd = open('chap9_madLibs.txt', mode='w')
fd.write(string)
fd.close()

# read newly created file --> new string
fd = open('chap9_madLibs.txt', mode='r')
string = fd.read()
fd.close()

# get user inputs (adjective, noun, verb, noun), uptade string.
for item in ['ADJECTIVE', 'NOUN', 'past tense VERB', 'NOUN']:  # using string.replace()
    prompt = 'enter a ' + item + ': '
    user_input = input(prompt)
    string = string.replace(item, user_input, 1)

# create new file with new string, output string to console
fd = open('chap_madLibs2.txt', mode='w')
fd.write(string)
fd.close()

print(string)
