
import pandas as pd
import re

filename = '/Users/steve/sun_also_rises.txt'

csv = []

with open(filename, "r") as myfile:
    lines = myfile.readlines()
    sentence_fragment = ''
    for i, line in enumerate(lines):
        line = re.sub(' +', ' ', line)
        line = re.sub('\n', '', line)
        sentences = line.split('.')
        sentences = [sent for sent in sentences if len(sent) > 0] # remove empty strings (e.g. if line ended with a '.')
        print(f"\n line {i}: {line}, len(line) = {len(line)}, numsent = {len(sentences)}")

        # don't bother with lines with 0 or 1 characters in them
        if len(line) <= 1:
            continue
       
        # check that this line has at least 2 or sentences (i.e. at least one period), or the line ends with a period
        if len(sentences) > 1:

            # put each of the 0, 1, .., n-1 sentences in our list of sentences
            for sent in sentences[:-1]:
                csv.append(str(sentence_fragment + sent + '.').lstrip())
                sentence_fragment = ''
                #print(f"\n   sentence: {sent + '.'}, len(sent) = {len(sent)}")

            # put remaining sentence in sentence fragement until next line (if there was no period on end of this line)
            if line[-1] != '.':
                sentence_fragment += sentences[-1] + ' '

        # there is only one sentence in this line
        if len(sentences) == 1:
            
            # this this sentence ends with a period, so add it to the csv file
            if line[-1] == '.':
                csv.append(str(sentence_fragment + sentences[0] + '.').lstrip())
                sentence_fragment = ''
                #print(f"\n   sentence: {sent + '.'}, len(sent) = {len(sent)}")
            else:
                sentence_fragment += sentences[0] + ' '

        
        #print(f"    m ={m} and len(m) = {len(m)}")
        #if i > 300:
        #    break 

myfile.close()

df = pd.DataFrame({'sentence':csv})
df.to_csv('/Users/steve/sunalsorises.csv', index=False)

#print(csv)