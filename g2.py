import re

# load in text
with open('debate.txt', 'r') as rf:
    text = rf.read() # set variable 'text' for debate.txt content
    words = text.replace("\n", " ")
    words2 = words.split(" ")
    # print(words2[0:500])
# break up text into words. Split by white space \s

# now we want all people's names 
names = re.findall(r'[A-Z]+?:\s', text)
names2 = list(dict.fromkeys(names)) # dictionaries cannot have duplicates. Remove duplicate names in list by forcing all names into dict, then put names back into list.
candidate = [] # look into every item in names2 and if you find a space, change it with nothing. Iterating over the list.
for name in names2: # name is now string
    candidate.append(name.replace(" ", "")) # thingyouusemethodwith.method
# print(candidate)

# Now the list candidate now matches many times to text. Between each match, take all items and join with spaces to form another string. cite https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/ 
# for loop for iteration. 

matches = []
for i in range(0, len(words2)): #for every item in words2, if it matches any items in candidate, give me its position
    if words2[i] in candidate: # words2[1] = HOLT. HOLT is in candidate. Meets criteria. Therefore, i (currently 1) is appended into matches.
        matches.append(i) # appends every position of a match. 
# print(matches)

# iterate through every index, list of names
name_list = []
for position in matches: 
    name = words2[position] # who's name is at certain position?
    #print (name + ' is at ' + str(position))
    name_list.append(name)
# print(name_list) # replaces all position numbers with names, 0 = Holt, 236 = Warren, so on

# now need to match every speak to its respective owner. Who says what in every position?
# automatically sorts snip into respective bin
# use a dict
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
counter = 0
targetWord = '(CROSSTALK)'
for pos in matches:
    #counter = 0
    #snip = words2[int(pos[counter + 0])+1 : int(pos[counter + 1])] # words spoken # attribute words spoken to correct person
    try:
      snip = words2[matches[counter + 0] : matches[counter + 1]] # words spoken # attribute words spoken to correct person
    except:
      pass # went past end of list
    try:
      #d[name_list[counter]].append(snip)
      d[name_list[counter]] = d[name_list[counter]] + snip
    except:
      pass
    counter = counter + 1

#print (' here is some nonsense that SANDERS said: ' + str(d['SANDERS:']))
# print (' here is some nonsense that WARREN said: ' + str(d['WARREN:']))

for name in candidate:
  try:
    print (name + ' got ' + targetWord + ' ' + str(d[name].count(targetWord)))
  except:
    # may fail such as in case of PROTESTORS
    pass

# 12 elifs
# condition st
# dictionary in which each of 12 talkers have a list of everytime they talk
# if there's a dict with Holt and everytime he speaks, that means you can make dict whose key is name of candidates, value is list of everytime they've spoken anything
# then go back to words2, using that info
# name_list = who said each index

# search for crosstalk, then done
