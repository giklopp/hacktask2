# run with 'python ripDebate.py'
import re, pprint

debug = False

with open('./debateWithSpaces.txt', 'r') as rf:
  text = rf.read()

#key: [total spoken lines, crosstalk events, total chars]
# removed names and set them dynamically ar runtime
'''
d = {'BIDEN': [0,0,0],
 'BLOOMBERG': [0,0,0],
 'SANDERS': [0,0,0],
 'WARREN': [0,0,0],
 'KLOBUCHAR': [0,0,0],
 'BUTTIGIEG': [0,0,0],
 'HOLT': [0,0,0]}
'''

d = {}
lCtr = 0
currentKeyName = ''

x = re.split('(\n[A-Z]*:)',text)
for line in x:
  if currentKeyName != '':
    # first see if there is a dict entry for this key.  If not, catch the error and create one
    try:
      test = d[currentKeyName]
    except:
      print ('Created dict entry for ' + currentKeyName)
      d[currentKeyName] = [0,0,0,'']  # adding a string to cobble it all together for linguistic complexity analysis
 
    try:
      d[currentKeyName][0] = d[currentKeyName][0] + 1
      if line.find('CROSSTALK') >= 0:
        d[currentKeyName][1] = d[currentKeyName][1] + 1
      d[currentKeyName][2] = d[currentKeyName][2] + len(line)
      d[currentKeyName][3] = d[currentKeyName][3] + ' ' + line
    except:
      pass
    currentKeyName = ''
  if line.endswith(':'):
    currentKeyName = line[0:len(line)-1].strip()
    if debug: print ('PROCESS line for ' + currentKeyName + ' ~ ' + x[lCtr + 1])
  lCtr = lCtr + 1


if debug: print ('\n - - - FINISHED ' + str(lCtr) + ' lines - - - \n')
print ('#output format is: PERSON, total spoken lines, crosstalk events, total chars, total words, average word length')
if debug: pprint.pprint(d)
for i in d:
  wordSalad = d[i][3].split()
  totalWords = len(wordSalad)
  sum = 0
  for word in wordSalad:
        ch = len(word)
        sum = sum + ch
  avg = float(sum) / totalWords
  # csv compatible formatting
  print (i + ',' + str(d[i][0]) + ',' + str(d[i][1]) + ',' + str(d[i][2]) + ',' + str(totalWords) + ',' + str(round(avg,2)))


