# run with 'python ripDebate.py'
# tested with python 2.7

import this, re, pprint

debug = False  # set debug true for some extra output at runtime

# set your debate text file.  NOTE: must be properly formatted for the regex split to work as expected
#with open('./debate2WithSpaces.txt', 'r') as rf:  # dem debate #10 (Charleston)
with open('./debateWithSpaces.txt', 'r') as rf:  # dem debate #9 (Vegas)
  text = rf.read()

d = {}  # hold all the data here using NAME as the key
lCtr = 0  # a line counter, not used for much but a sanity check
currentKeyName = '' # holds the current key name as we iterate thru the text data

x = re.split('(\n[A-Z]*:)',text)  # chop up the data with re using NAME:

for line in x:  # look at each chunk of the split up file

  if currentKeyName != '':
    # see if there is already a dict entry for this key.  If not, catch the error and create one
    try:
      test = d[currentKeyName]
    except:
      print ('Created dict entry for ' + currentKeyName)
      d[currentKeyName] = [0,0,0,'']  # adding a string to cobble it all together for linguistic complexity analysis
 
    try:  # populate the data here
      d[currentKeyName][0] = d[currentKeyName][0] + 1
      if line.find('CROSSTALK') >= 0:
        d[currentKeyName][1] = d[currentKeyName][1] + 1
      d[currentKeyName][2] = d[currentKeyName][2] + len(line)
      d[currentKeyName][3] = d[currentKeyName][3] + ' ' + line
    except:
      pass
    currentKeyName = ''  # reset currentKeyName for the next chunk

  if line.endswith(':'):
    currentKeyName = line[0:len(line)-1].strip()
    if debug: print ('PROCESS line for ' + currentKeyName + ' ~ ' + x[lCtr + 1])
  lCtr = lCtr + 1


print ('\n - - - FINISHED ' + str(lCtr) + ' lines - - - \n')
print ('#output format is: PERSON, total spoken lines, crosstalk events, total chars, total words, average word length')
# write this to a file
output = open("results.csv", "a")
if debug: pprint.pprint(d)
for i in sorted(d):  # for extra credit add some word stats
  wordSalad = d[i][3].split()
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
print('finished!  results are in result.csv')


