import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import RetrieveAndRankV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='1a0b77b6-b49b-48cb-866a-0077f016a506',
  password='v88OuvDlfLcQ')

#classify function
def classify(id, question):
    classes = natural_language_classifier.classify(id, question)
    j = json.loads(json.dumps(classes))
    class_name = j['top_class']
    return class_name

#RR function
def retrieveRank(question, topic):
    with open('credentials.json') as credentials_file:
        credentials = json.load(credentials_file)
    retrieve_and_rank = RetrieveAndRankV1(
        username=credentials['username'],
        password=credentials['password'])
    # Replace with your own solr_cluster_id
    solr_cluster_id = 'scff1b48f6_5178_4c7c_bac8_39fffaf6f83f'

    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, topic)
    # Can also refer to config by name

    # Example search
    results = pysolr_client.search(question)

    #print results.docs
    return results.docs
    #return results.docs[0]['body'][0]
    #return results.docs[0]['body'][0].split(',')[0].split(':')[1]

#get the question
question = raw_input('ask your question: ')

##classify the question
topic = classify('cedf17x168-nlc-108', question)

print(topic)
answer = retrieveRank(question, topic)

print(answer)

#whats a semicolon?

#chance of thunderstorm?
#how cold today?




