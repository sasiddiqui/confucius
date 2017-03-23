import json
#from watson_developer_cloud import RetrieveAndRankV1
from ConfuciusRR import ConfuciusRetrieveAndRankV1
#%%

with open('../../resources/config/rr-config.json') as rr_config:
    config = json.load(rr_config)
retrieve_and_rank = ConfuciusRetrieveAndRankV1(
    username = config['credentials']['username'],
    password= config['credentials']['password'])

#%%
# Solr clusters

solr_clusters = retrieve_and_rank.list_solr_clusters()
print(json.dumps(solr_clusters, indent=2))
#%%
created_cluster = retrieve_and_rank.create_solr_cluster(cluster_name='Test Cluster', cluster_size='1')
print(json.dumps(created_cluster, indent=2))
#%%
# Replace with your own solr_cluster_id
solr_cluster_id = 'sc0cbccce5_6f9c_41fa_86c5_1532f6a45e64'

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
collection = retrieve_and_rank.create_collection(solr_cluster_id, 'cse1223_raw_text', 'solr_config')
print(json.dumps(collection, indent=2))
#%%
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
print(json.dumps(collections, indent=2))

#%%
deleted_response = retrieve_and_rank.delete_collection(solr_cluster_id, 'ai', 'solr_config')
print(json.dumps(deleted_response, indent=2))
#%%
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'cse1223_raw_text')
#%%
# Can also refer to config by name


pysolr_client.add(output['documents'])
#%%
#Example search
results = pysolr_client.search("Are there any office hours for this course ?")
print('{0} documents found'.format(len(results.docs)))
print(json.dumps(results.docs,indent=2))

#%%
with open('sample_document.json') as docs_file:    
    documents = json.load(docs_file)
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'programming')
pysolr_client.add(documents['documents'])
#%%
results = pysolr_client.search("_version:e832c5a0-96b0-4cd8-8e8c-0bdb89f65104")
print('{0} documents found'.format(len(results.docs)))
print(results.docs)
#%%
# Rankers

rankers = retrieve_and_rank.list_rankers()
print(json.dumps(rankers, indent=2))
ranker_id = rankers['rankers'][0]['ranker_id']
#%%
#create a ranker
with open('ranker_training_data.csv', 'rb') as training_data:
    print(json.dumps(retrieve_and_rank.create_ranker(training_data=training_data, name='Ranker Test'), indent=2))
#%%
# replace YOUR RANKER ID
status = retrieve_and_rank.get_ranker_status('1eec74x28-rank-2104')
print(json.dumps(status, indent=2))
#%%
#Delete a ranker
delete_results = retrieve_and_rank.delete_ranker("1eec74x28-rank-2165")
print(json.dumps(delete_results))
#%%1eec7cx29-rank-328
# replace '42AF7Ex10-rank-47' with your ranker_id
with open('ranker_answer_data.csv', 'rb') as answer_data:
    ranker_results = retrieve_and_rank.rank('766366x22-rank-3332', answer_data)
    print(json.dumps(ranker_results, indent=2))
#%%
solr_cluster_id = 'sc0cbccce5_6f9c_41fa_86c5_1532f6a45e64'
ranker_id = '1eec74x28-rank-2104'
#data = {'answers': + 10}
url = '/v1/solr_clusters/'+solr_cluster_id+'/solr/'+'music'+'/fcselect?q='+'What the notes of music ?'+'&ranker_id='+ranker_id
results = retrieve_and_rank.request(method='GET',url=url,accept_json=False)
#%%
solr_cluster_id = 'sc0cbccce5_6f9c_41fa_86c5_1532f6a45e64'
ranker_id = '1eec74x28-rank-2104'
results = retrieve_and_rank.rank(solr_cluster_id, ranker_id, 'music', 'What are the notes of music ?')