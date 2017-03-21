import time
import json
from watson_developer_cloud import RetrieveAndRankV1
#%%
root = '../../'
with open(root + 'sandbox/ranker-test/rr-config-reddit.json') as rr_config:
    config = json.load(rr_config)
retrieve_and_rank = RetrieveAndRankV1(
    username = config['credentials']['username'],
    password= config['credentials']['password'])
#%%
#Create a new cluster
cluster_name = config['solr_cluster_name']
solr_clusters_list = retrieve_and_rank.list_solr_clusters()
exists = False
solr_cluster = {}
for item in solr_clusters_list['clusters']:
    if(item['cluster_name'] == cluster_name):
        exists = True
        solr_cluster = item
        break
if(exists):
    #print(json.dumps(solr_cluster, indent=2))
    print(solr_cluster['cluster_name'] + ' already exists')
#%%
#Upload the solf config file
solr_config_list = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
solr_config_name = config['solr_config_file'].split('.')[0]
exists = False
for item in solr_config_list['solr_configs']:
    if(item == solr_config_name):
        exists = True
        break
if(exists):
    print('Solr config has already being uploaded')
#%%
#Create the collections
collection_list = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
for item in config['collections']:
    collection_name = item['name']
    data_file_name = root + item['file_name']
    with open(data_file_name) as data_file:    
        raw_data = json.load(data_file)
        data = raw_data['documents']
    print('Loaded :' + str(len(data)) + ' records from ' + data_file_name)
    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, collection_name)
    num = 100 #Records to be uploaded per iteration
    rem = len(data)%num
    if(len(data)%num != 0 ):
        response = pysolr_client.add(data[0:rem])
        pysolr_client.commit()
        print('Uploaded ' + str(rem) +'/' + str(len(data)) + ' records')
    for i in range(rem, len(data),num):
        response = pysolr_client.add(data[i:i+num])
        pysolr_client.commit()
        print('Uploaded ' + str(i+num) +'/' + str(len(data)) + ' records')