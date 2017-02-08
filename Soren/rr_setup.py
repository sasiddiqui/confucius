'''
Script to setup the Solr Cluster and a Collection on IBM Bluemix
'''
import time
import json
from watson_developer_cloud import RetrieveAndRankV1
#%%
with open('rr-config.json') as rr_config:
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
    print(json.dumps(solr_cluster, indent=2))
    print('Cluster already exists')
else:
    solr_cluster = retrieve_and_rank.create_solr_cluster(cluster_name=cluster_name, cluster_size='1')
    print(json.dumps(solr_cluster, indent=2))
    status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster['solr_cluster_id'])
    while(status['solr_cluster_status'] != 'READY'):
        time.sleep(5)
        print('Waiting for cluster to get ready')
        print('Cluster Status: ' + status['solr_cluster_status'])
        status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster['solr_cluster_id'])
    print('Cluster Status: ' + status['solr_cluster_status'])
    print('Cluster created')
solr_cluster_id = solr_cluster['solr_cluster_id']
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
else:
    with open(config['solr_config_file'], 'rb') as solr_config_file:
        
        config_status = retrieve_and_rank.create_config(solr_cluster_id, solr_config_name, solr_config_file)
        print(config_status['message'])
#%%
#Create the collections
def object_pairs_hook(pair):
#    print('Read:')
#    print(pair)
    if(pair[0][0] == 'doc'):
        return pair[0][1]
    if(pair[0][0] == 'add'):
        return [item[1] for item in pair]
    d={}    
    for item in pair:
        d.update({item[0]:item[1]})
#    print('Parsed as:')
#    print(print(json.dumps(d,indent=2)))
    return d
collection_list = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
for item in config['collections']:
    collection_name = item['name']
    try:
        collection_list['collections'].index(collection_name)
        print(collection_name + ' already exists as a collections')
    except ValueError:
        collection = retrieve_and_rank.create_collection(solr_cluster_id, collection_name, solr_config_name)
        print('Created Collection ' + collection_name )
        data_file_name = item['file_name']
        with open(data_file_name) as data_file:    
            decoder = json.JSONDecoder(object_pairs_hook=object_pairs_hook)
            data_str = data_file.read()
            data = decoder.decode(data_str)
        print('Loaded :' + str(len(data)) + ' records from ' + data_file_name)
        pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, collection_name)
        for i in range(0, len(data),10):
            response = pysolr_client.add(data[i:i+10])
    #        print(response)
            pysolr_client.commit()
            print('Uploaded ' + str(i+10) +'/' + str(len(data)) + ' records')