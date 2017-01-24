import json
from watson_developer_cloud import RetrieveAndRankV1

with open('credentials.json') as credentials_file:    
    credentials = json.load(credentials_file)
#%%
retrieve_and_rank = RetrieveAndRankV1(
    username = credentials['username'],
    password= credentials['password'])

#%%
# Solr clusters

solr_clusters = retrieve_and_rank.list_solr_clusters()
print(json.dumps(solr_clusters, indent=2))
#%%
created_cluster = retrieve_and_rank.create_solr_cluster(cluster_name='Test Cluster', cluster_size='1')
print(json.dumps(created_cluster, indent=2))
#%%
# Replace with your own solr_cluster_id
solr_cluster_id = 'scff1b48f6_5178_4c7c_bac8_39fffaf6f83f'

status = retrieve_and_rank.get_solr_cluster_status(
    solr_cluster_id=solr_cluster_id)
print(json.dumps(status, indent=2))
#%%
# Solr cluster config
with open('solr_config.zip', 'rb') as config:
    config_status = retrieve_and_rank.create_config(solr_cluster_id,'test-config', config)
    print(json.dumps(config_status, indent=2))
#%%
deleted_response = retrieve_and_rank.delete_config(solr_cluster_id, 'test-config')
print(json.dumps(deleted_response, indent=2))
#%%
configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
print(json.dumps(configs, indent=2))
#%%
collection = retrieve_and_rank.create_collection(solr_cluster_id, 'test-collection', 'test-config')
print(json.dumps(collection, indent=2))
#%%
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
print(json.dumps(collections, indent=2))

#%%
deleted_response = retrieve_and_rank.delete_collection(solr_cluster_id, 'test-collection', 'test-config')
print(json.dumps(deleted_response, indent=2))
#%%
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, collections['collections'][0])
# Can also refer to config by name

#Example search
pysolr_client.add([{'id': '1', 'body':'Who is the father of computing ?'}])
results = pysolr_client.search('who discovered computers ?')
print('{0} documents found'.format(len(results.docs)))
print(results.docs)

#%%
# Rankers

rankers = retrieve_and_rank.list_rankers()
print(json.dumps(rankers, indent=2))
#%%
#create a ranker
with open('ranker_training_data.csv', 'rb') as training_data:
    print(json.dumps(retrieve_and_rank.create_ranker(training_data=training_data, name='Ranker Test'), indent=2))
#%%
# replace YOUR RANKER ID
status = retrieve_and_rank.get_ranker_status('766366x22-rank-3332')
print(json.dumps(status, indent=2))
#%%
# delete_results = retrieve_and_rank.delete_ranker('YOUR RANKER ID')
# print(json.dumps(delete_results))

# replace '42AF7Ex10-rank-47' with your ranker_id
with open('../resources/ranker_answer_data.csv', 'rb') as answer_data:
    ranker_results = retrieve_and_rank.rank('42AF7Ex10-rank-47', answer_data)
    print(json.dumps(ranker_results, indent=2))
