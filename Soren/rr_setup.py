'''
Script to setup the Solr Cluster and a Collection on IBM Bluemix
'''
import json
from watson_developer_cloud import RetrieveAndRankV1
credentials_string = '''{
  "url": "https://gateway.watsonplatform.net/retrieve-and-rank/api",
  "password": "ANlCCDTtOHr4",
  "username": "55729e6b-2d18-46f8-b6a0-3e87cdd80797"
}'''

retrieve_and_rank = RetrieveAndRankV1(
    username = credentials['username'],
    password= credentials['password'])
#%%
cluster_name = 'Test Cluster'
created_cluster = retrieve_and_rank.create_solr_cluster(cluster_name=cluster_name, cluster_size='1')
solr_cluster_id = created_cluster['solr_cluster_id']
print('Created Cluster')
print('Name: ' + clusterName)
print('ID: ' + solr_cluster_id)
print('Size: ' + created_cluster['cluster_size'])
status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
while(status['solr_cluster_status'] != 'READY'):
    print('Waiting for ' + clusterName + ' to get ready')
    print('Cluster Status: ' + status['solr_cluster_status'])
    status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
print('Cluster Status: ' + status['solr_cluster_status'])
#%%
with open('solr_config.zip', 'rb') as config:
    config_status = retrieve_and_rank.create_config(solr_cluster_id,'test-config', config)
    print(config_status['message'])
#%%
collection_name = 'AI'
collection = retrieve_and_rank.create_collection(solr_cluster_id, collection_name, 'test-config')
if(collection.status['success']):
    print('Created Collection ' + collection_name )
else:
    print('Failed to Create Collection ' + collection_name)
#%%    
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, collection_name)