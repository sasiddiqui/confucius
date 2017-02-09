# Parses a Posts.xml file into three input files, for NLC, retrieve, and rank

import json, csv, sys
import xml.etree.ElementTree as ET



if __name__ == '__main__':
    docName = sys.argv[1]
    #Create NLC document, retrieve document, ranker csv
    nlc = open(docName + '.nlc.csv', 'w+')
    nlcWrite = csv.writer(nlc)

    retrieveData = {}
    retrieveData['documents'] = []

    rankData = {}

    tree = ET.parse(docName) #opens the input xml file
    root = tree.getroot()

    questions = {} # maps question IDs to question text


    #iterate through all row elements children of post element
    for post in root:
        if post.attrib["PostTypeId"] == '1':  #if post is question
            #add to NLC file


            #Was having a unicode issue but solved it with this encode method
            nlcWrite.writerow(["\"" + post.attrib['Body'] + "\"", "ai"])
            questions[post.attrib['Id']] = post.attrib['Body']
            rankData[post.attrib['Body']] = []

        elif post.attrib["PostTypeId"] == '2': #post is an answer
            parentQ = questions[post.attrib['ParentId']]


            #Added commas between the elements here
            retrieveData['documents'].append({'id': post.attrib['Id'],
                                              'body': {
                                                'question' : parentQ ,
                                                'answer' : post.attrib['Body']
                                              }})

            rankData[parentQ].append((post.attrib['Id'], post.attrib['Score']))

    # Create and write to JSON file for retriever
    retriever = open(docName + '.retrieve.json', 'w+')
    json.dump(retrieveData, retriever, indent=4)

    # Convert rankData to appropriate format and write CSV file
    sortedLists = []
    for q in rankData:

        #Had sortedList = rankData[q].sort(key=lambda tup: tup[1], reverse=True)
        #but since the .sort method doesnt return a list I changed it to:
        sortedList = sorted(rankData[q], key=lambda tup: int(tup[1]), reverse=True)
        row = [q]
        row.extend(map(lambda tup: tup[0], sortedList))
        sortedLists.append(row)

    ranker = open(docName + '.ranker.csv', 'w+')
    rankerWrite = csv.writer(ranker)
    rankerWrite.writerows(sortedLists)
