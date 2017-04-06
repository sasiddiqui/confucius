import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from source.rr.ConfuciusRR import ConfuciusRetrieveAndRankV1

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
def retrieve(question, topic):
    with open('resources/config/rr-config.json') as credentials_file:
        credentials = json.load(credentials_file)

    retrieve_and_rank = ConfuciusRetrieveAndRankV1(
        username=credentials['credentials']['username'],
        password=credentials['credentials']['password'])

    solr_clusters = retrieve_and_rank.list_solr_clusters()
    solr_cluster_id = solr_clusters['clusters'][1]['solr_cluster_id']

    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, topic)
    # Can also refer to config by name

    # Example search
    results = pysolr_client.search(question)
    return retrieve_and_rank.removeCharTags(results.docs[0]['body'][0])

def rank(question, topic):
    with open('resources/config/rr-config.json') as credentials_file:
        credentials = json.load(credentials_file)

    retrieve_and_rank = ConfuciusRetrieveAndRankV1(
        username=credentials['credentials']['username'],
        password=credentials['credentials']['password'])

    solr_clusters = retrieve_and_rank.list_solr_clusters()
    solr_cluster_id = solr_clusters['clusters'][1]['solr_cluster_id']

    ranker_id = '1eec74x28-rank-2104'
    results = retrieve_and_rank.rank(solr_cluster_id, ranker_id, topic, question)
    return retrieve_and_rank.removeCharTags(results[0]['body'])
    
# def get_topic(question, id):
#     topic = classify(id, question)
#     return topic
#
# def get_answer(question, id):
#     topic = classify(id, question)
#     answer = retrieveRank(question, topic).replace("\\n", "").replace("u'","").replace("answer':", "")
#     return answer

if __name__ == '__main__':
    #get the question
    question = raw_input('ask your question: ')

    #classify the question
    topic = classify('90e7acx197-nlc-170', question)
    print 'the topic is {0}'.format(topic)

    answer = retrieve(question, topic).replace("\\n", "").replace("u'","").replace("answer':", "")
    answerRank = rank(question, topic).replace("\\n", "").replace("u'","").replace("answer':", "")
    print answer
    print('')
    print answerRank

    # response = raw_input('is this what you were looking for?')
    # if response == 'no':
    #     newTopic = raw_input('please enter the new topic')
    #     answer = rank(question, newTopic.replace("\\n", "").replace("u'", "").replace("answer':", ""))
    #     print answer



