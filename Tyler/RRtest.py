from watson_developer_cloud import RetrieveAndRankV1
import json


with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
retrieve_and_rank = RetrieveAndRankV1(
    username=credentials['username'],
    password=credentials['password'])
# Replace with your own solr_cluster_id
solr_cluster_id = 'scff1b48f6_5178_4c7c_bac8_39fffaf6f83f'


#ADD WEATHER
collection = retrieve_and_rank.create_collection(solr_cluster_id, 'weather', 'test-config')
with open('sample_document2.json') as docs_file:
    documents = json.load(docs_file)
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'weather')
pysolr_client.add(documents['documents'])

#DELETE
#retrieve_and_rank.delete_collection(solr_cluster_id, 'weather', 'test-config')


#LIST COLLECTIONS
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
print(json.dumps(collections, indent=2))