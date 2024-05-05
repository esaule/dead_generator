import syllables
import re
import cmudict

import nltk
from nltk.tokenize import word_tokenize

if False:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('cmudict')

# Load the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Function to check if two words rhyme the same
def rhyme_same(word1, word2):
    # Convert the words to lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    # If both words are in the dictionary
    if word1 in pronouncing_dict and word2 in pronouncing_dict:
        # Get the pronunciation of both words
        pronunciation1 = pronouncing_dict[word1][0]
        pronunciation2 = pronouncing_dict[word2][0]
        # Check if they have the same ending pronunciation
        return pronunciation1[-2:] == pronunciation2[-2:]
    else:
        return False

  
# Define your regular expression pattern
patterns = [re.compile(r'.*ted$')  ]

syllablecount = 3
#basewords = ['infested']
basewords = ['infested']

# Open the file
with open('american-english', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        line = line.strip()
        matched = False
        for p in patterns:
            if p.match(line):
                matched = True
                break

        if matched:
            if syllables.estimate(line) != syllablecount:
                matched = False
        if matched:
            matched = False
            for bw in basewords:
                if rhyme_same (bw, line):
                    matched = True
            
                
        if matched:
            print(line)

