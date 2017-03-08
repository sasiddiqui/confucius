import sys
import json
#%%
fileName = 'data.txt'
with open(fileName) as file:
    lines = file.readlines()

#We can group sentences according to structure. This would be easier if we parse HTML data.
#For now the data corpus will contain - single sentences, paragraphs and headings
#%%
dataByPara = lines
dataByLine = []
for line in dataByPara:
    dataByLine = dataByLine + line.split('.')

dataAll = dataByPara + dataByLine

#The data contains many short strings - e.g empty lines, split up email address 
#and urls. These have to be cleaned. But I am not doing that for now

output = []
id = 1
for item in dataAll:
    output = output + [{'id': id, 'body':item}]
    id = id + 1
#%%
output = {'documents': output}
with open(fileName + '.json','w') as file:
    file.write(json.dumps(output,indent=2))
    