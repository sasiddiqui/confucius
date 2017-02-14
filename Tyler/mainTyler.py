'''import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import RetrieveAndRankV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='74173aac-8171-4054-b2db-fa873012069e',
  password='OKwSvr3BdvKc')

#classify function
def classify(id, question):
    classes = natural_language_classifier.classify(id, question)
    j = json.loads(json.dumps(classes))
    class_name = j['top_class']
    return class_name

#RR function
def retrieveRank(question, topic):
    with open('rr-config.json') as credentials_file:
        credentials = json.load(credentials_file)
    retrieve_and_rank = RetrieveAndRankV1(
        username=credentials['credentials']['username'],
        password=credentials['credentials']['password'])
    # Replace with your own solr_cluster_id
    solr_clusters = retrieve_and_rank.list_solr_clusters()
    solr_cluster_id = solr_clusters['clusters'][0]['solr_cluster_id']

    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, topic.upper())
    # Can also refer to config by name

    # Example search
    results = pysolr_client.search(question)

    #print results.docs
    return results.docs
    #return results.docs[0]['body'][0]
    #return results.docs[0]['body'][0].split(',')[0].split(':')[1]

#get the question
question = raw_input('ask your question: ')

#classify the question
topic = classify('f5b432x172-nlc-3555', question)

print('the topic is ' + topic)


answer = retrieveRank(question, topic)

print(answer)

print('')
response = raw_input('is this what you were looking for?')
if response == 'no':
    newTopic = raw_input('please enter the new topic')
    answer = retrieveRank(question, newTopic)
    print(answer)


#whats a semicolon?
#chance of thunderstorm?
#how cold today?

'''


