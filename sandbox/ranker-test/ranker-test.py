import json
from watson_developer_cloud import RetrieveAndRankV1

#%%
with open('../../resources/config/rr-config.json') as rr_config:
    config = json.load(rr_config)
    retrieve_and_rank = RetrieveAndRankV1(
    username = config['credentials']['username'],
    password= config['credentials']['password'])

#%%
# Solr clusters
solr_clusters = retrieve_and_rank.list_solr_clusters()
solr_cluster_id = [ cluster['solr_cluster_id'] for cluster in solr_clusters['clusters'] if cluster['cluster_name'] == 'Test Cluster' ][0]
status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
print(json.dumps(status, indent=2))

#%%
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)['collections']
print(json.dumps(collections, indent=2))

#%%
#Simple Retive Sarch
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'AI')
results = pysolr_client.search('who discovered computers ?')
print('{0} documents found'.format(len(results.docs)))
results = [item['id'] for item in results.docs]
print(results)

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
status = retrieve_and_rank.get_ranker_status('1eec74x28-rank-1706')
print(json.dumps(status, indent=2))
#%%
#Delete a ranker
delete_results = retrieve_and_rank.delete_ranker("1eec7cx29-rank-328")
print(json.dumps(delete_results))
#%%1eec7cx29-rank-328
# replace '42AF7Ex10-rank-47' with your ranker_id
with open('ranker_answer_data.csv', 'rb') as answer_data:
    ranker_results = retrieve_and_rank.rank('766366x22-rank-3332', answer_data)
    print(json.dumps(ranker_results, indent=2))
#%%
ranker_id = '1eec74x28-rank-1706'
data = {'answers': + 10}
url = '/v1/solr_clusters/'+solr_cluster_id+'/solr/'+'AI'+'/fcselect?q='+'What is a backprop'+'&ranker_id='+ranker_id
results = retrieve_and_rank.request(method='GET',url=url,accept_json=False)