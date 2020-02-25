'''
HACKTASK 2
# I want to write a short Python script that uses regular expressions to extract information from the full transcript of the Ninth Democratic debate in Las Angeles, from February 19, 2020. 
# First, turn this script from https://www.nbcnews.com/politics/2020-election/full-transcript-ninth-democratic-debate-las-vegas-n1139546 into a text file
# Find the number of instances of crosstalk for each person, displayed on csv file.
'''

import re

# load in text (should this be loaded in at end?)
with open('debate.txt', 'r') as rf:
    text = rf.read() # set variable 'text' for debate.txt content

# Design a regular expression that matches names
'''
([A-Z]+?): # use regex to match names: capital letters followed by a :
'''
name_regex = re.compile(r'^[A-Z]+?:', re.M) # multi-line regex
snippets = name_regex.split(text) # take txt and return a list in which every other item is a candidate's dialogue and the other is the names # split: first item will be blank. Second item will be Holt's dialogue.






# make list that has all 11 names
name_list = ["HOLT", "TODD", "JACKSON", "HAUC", "RALSTON", "SANDERS", "KLOBUCHAR", "WARREN", "BUTTIGEG", "BIDEN", "BLOOMBERG"]
name_list = []
name_list = name_regex #???

# for loop to make machine compile everything each candidate says into one string so machine will know where crosstalk is relative to candidate
for name_list in snippets:
    if name_list
# I don't know how to do this. What exactly does this give me? How do I bring (CROSSTALK) into for loop?








# Make a crosstalk counter for loop

crosstalk_count = 0 # variable to track how often (CROSSTALK) occurs
for page in snippets: # is page correct? Should I be using snippets?
    if 
'''
someCtr = 0
someString.find('CROSSTALK'):
  someCtr = someCtr + 1
'''
# example of finding a word and then counting it into indexCount
string1 = "help me"
string2 = "help"
string3 = string1.split()
indexCount = 0
for word in string2:
    if word == string3:
        print("Your word was found at index point", int(indexCount)))
    else:
        print("Your word was not found at", int(indexCount))
    indexCount += 1 # adds 1 to a count everytime loop starts again

# another old example using frequency
MCC = [] # Most common character variable
MCCFreq = 0 # Variable to track how often chracter occurs

for char in contents: # For loop to iterate through all chars in monkey.txt, one at a time.
    if char.isalnum(): # If the character currently being analyzed by computer is alphanumeric...
        freq = contents.count(char) #...then count this character's frequency and label the resulting number as variable 'freq'.
        if freq > MCCFreq: # If this freq is greater than current number assigned to MCCFreq...
            MCCFreq = freq #...then assign freq as value for MCCFreq.
        elif freq == MCCFreq: # If one particular character has the same highest frequency as another character...
            if char not in MCC: # ...then, if this character is not already in the MCC list... 
                MCC.append(char) # append MCC list by adding this character alongside the other highest frequency character.





# should now have TWO LISTS: list of 11 items, and then another list of 11 items that will display a number (representing amount of times crosstalk appears in script)
# must zip/combine the two lists. 
name_list = []
crosstalk_count = []
# list of tuples from name_list and crosstalk_count # tuples??
list(zip(name_list, crosstalk_count))
# or should I use map lambda? Is map lambda only for when lengths of original lists do not match?
combined_list = map(lambda x,y: (x,y), name_list, crosstalk_count)






# Third, create a dictionary with people's names +- one everytime you see (CROSSTALK) in order to find instances of (CROSSTALK) per person.
name_to_crosstalk = {[combined_list]} # i dunno






# Fourth, put all info into csv, f string, write results into a file
with open("candidatecrosstalk.csv", 'w') as wf:
    # Write a header:
    wf.write("Title, HOLT, TODD, JACKSON, HAUC, RALSTON, SANDERS, KLOBUCHAR, WARREN, BUTTIGEG, BIDEN, BLOOMBERG\n") 
    # write the data
    wf.write("frequency of crosstalk") # unsure how to do use zipped file, will work on later