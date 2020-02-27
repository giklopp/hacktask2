import re

# load in text
with open('debate.txt', 'r') as rf: # rf is your reference to that file, so anything you will do with that file starts with rf
    text = rf.read() # set variable 'text' for debate.txt content
    words = text.replace("\n", " ") # too complicated. Don't need to remove hard returns. Actual splitting of string itself is unecessary.
    words2 = words.split(" ") 
# break up text into words. Split by white space \s

# now we want all people's names 
names = re.findall(r'[A-Z]+?:\s', text)
names2 = list(dict.fromkeys(names)) # dictionaries cannot have duplicates. Remove duplicate names in list by forcing all names into dict, then put names back into list.
candidate = [] # look into every item in names2 and if you find a space, change it with nothing. Iterating over the list. This is my unique list of candidates.
for name in names2: # name is now string
    candidate.append(name.replace(" ", "")) # thingyouusemethodwith.method
# research strip command

matches = []
for i in range(0, len(words2)): #for every item in words2, if it matches any items in candidate, give me its position
    if words2[i] in candidate: # words2[1] = HOLT. HOLT is in candidate. Meets criteria. Therefore, i (currently 1) is appended into matches.
        matches.append(i) # appends every position of a match. 
# I end up with a long list (matches) of positions where you find words like SANDERS: or HOLT: etc

# iterate through every index, list of names
name_list = []
for position in matches: 
    name = words2[position] # who's name is at certain position?
    name_list.append(name)
# print(name_list) # replaces all position numbers with names, 0 = Holt, 236 = Warren, so on

# now need to match every speak to its respective owner. Who says what in every position?
# automatically sorts snip into respective bin
# create dict to hold all this garbage
d = {
 'HOLT:':  [],
 'TODD:': [],
 'JACKSON:': [],
 'HAUC:': [],
 'RALSTON:': [],
 'SANDERS:': [],
 'KLOBUCHAR:': [],
 'WARREN:': [],
 'BUTTIGIEG:': [], 
 'BIDEN:': [],
 'BLOOMBERG:': [],
 'PROTESTORS:': [],
}
# iterate through all matches again with counter. Need a TARGET WORD.
# except/pass = a way to have sloppy code that doesn't crash your script
counter = 0
targetWord = '(CROSSTALK)'
for pos in matches:
    try:
        snip = words2[matches[counter] : matches[counter + 1]] # words spoken # attribute words spoken to correct person
        # we want all words between first and next position. Snip is words2 at current match to next match. 
    except: 
      pass # went past end of list
    try: # try/accept. Swallows errors. 
      d[name_list[counter]] = d[name_list[counter]] + snip # dictionary has keys and values. Keys are names. Values is long list of strings. Take dictionary, set that key to a value. That value is current value + snip
      # then we have to iterate the counter.
    except:
      pass
    counter = counter + 1 # otherwise it will do the same thing over and over again. Would get to end of matches but would keep adding the same first position into whosever name.
# this is the population of the dictionary. Have everything each person said keyed to their name.

# print (' here is some stuff that SANDERS said: ' + str(d['SANDERS:']))
#print (' here is some stuff that SANDERS said: ' + str(d['SANDERS:']))
# print (' here is some stuff that WARREN said: ' + str(d['WARREN:']))
# these are just fun tests

for name in candidate:
  try:
    print (name + ' got ' + targetWord + ' ' + str(d[name].count(targetWord)))
    print (i + ',' + str(d[i].count(targetWord)))
  except:
    pass

print ('This shows person--moderator or candidate--, and his/her total instances of crosstalk')
# Hooray, this gives me a nice terminal result linking each speaker to their instances of crosstalk.
# Now I want to put it into a table.

output = open("crossfirehurricane.csv", "a") # append to end of existing file
output.write('speaker, total instances of crosstalk') # header line
# output is file handler

'''
for i in sorted(d):  # for extra credit add some word stats
  wordSalad = d[i][3].split() # i is dict key. 
  totalWords = len(wordSalad)
  sum = 0
  for word in wordSalad:
        ch = len(word)
        sum = sum + ch
  avg = float(sum) / totalWords
  # csv compatible formatting
  print (i + ',' + str(d[i][0]) + ',' + str(d[i][1]) + ',' + str(d[i][2]) + ',' + str(totalWords) + ',' + str(round(avg,2)))
  output.write(i + ',' + str(d[i][0]) + ',' + str(d[i][1]) + ',' + str(d[i][2]) + ',' + str(totalWords) + ',' + str(round(avg,2)) + '\n')
output.close()
print('finished!  results are in results.csv')
'''
