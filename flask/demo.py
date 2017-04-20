import json
import os
from watson_developer_cloud import NaturalLanguageClassifierV1
from ConfuciusRR import ConfuciusRetrieveAndRankV1

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
    with open('rr-config.json') as credentials_file:
        credentials = json.load(credentials_file)

    retrieve_and_rank = ConfuciusRetrieveAndRankV1(
        username=credentials['credentials']['username'],
        password=credentials['credentials']['password'])

    #solr_clusters = retrieve_and_rank.list_solr_clusters()
    #solr_cluster_id = solr_clusters['clusters'][1]['solr_cluster_id']
    solr_cluster_id = 'scc3ecccbb_2901_4275_b4d7_11342899dca1'

    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, topic)
    # Can also refer to config by name

    # Example search
    results = pysolr_client.search(question)
    return retrieve_and_rank.removeCharTags(results.docs[0]['body'][0].split("', 'question",1)[0])

#rank function
def rank(question, topic):
    with open('rr-config.json') as credentials_file:
        credentials = json.load(credentials_file)

    retrieve_and_rank = ConfuciusRetrieveAndRankV1(
        username=credentials['credentials']['username'],
        password=credentials['credentials']['password'])

    #solr_clusters = retrieve_and_rank.list_solr_clusters()
    #solr_cluster_id = solr_clusters['clusters'][1]['solr_cluster_id']
    solr_cluster_id = 'scc3ecccbb_2901_4275_b4d7_11342899dca1'

    ranker_id = '1eec74x28-rank-5332'
    results = retrieve_and_rank.rank(solr_cluster_id, ranker_id, topic, question)
    return (retrieve_and_rank.removeCharTags(results[0]['body']), retrieve_and_rank.removeCharTags(results[0]['confidence']))



def get_topic(question, id):
    #topic = classify(id, question)
    topic = 'reddit_data'
    return topic

def get_retrieve(question, id):
    #topic = classify(id, question)
    topic = 'reddit_data'
    answer = retrieve(question, topic).replace("\\n", "").replace("u'","").replace("answer':", "")
    return answer[4:]

def get_rank(question, id):
    #topic = classify(id, question)
    topic = 'reddit_data'
    t1,t2 = rank(question, topic)
    t1.replace("\\n", "").replace("u'","").replace("answer':","")
    return t1, t2


def remove_html():
    if os.path.exists("templates"):
        return True
    return False


if __name__ == '__main__':
    #get the question
    question = raw_input('ask your question: ')

    #classify the question
    #topic = classify('90e7acx197-nlc-170', question)
    topic = 'reddit_data'
    print 'the topic is {0}'.format(topic)
    t1,t2 = get_rank(question, 2)
    print t1
    print ''
    print t2




