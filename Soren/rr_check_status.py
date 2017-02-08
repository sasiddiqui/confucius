#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check the information about the Retrive and Rank Service

Created on Tue Feb  7 16:07:57 2017

@author: soren
"""
#%%
import sys
import time
import json
from watson_developer_cloud import RetrieveAndRankV1
with open('rr-config.json') as rr_config:
    config = json.load(rr_config)
retrieve_and_rank = RetrieveAndRankV1(
    username = config['credentials']['username'],
    password= config['credentials']['password'])
#%%
cluster_name = config['solr_cluster_name']
solr_clusters_list = retrieve_and_rank.list_solr_clusters()
print(json.dumps(solr_clusters_list, indent=2))
exists = False
solr_cluster = {}
for item in solr_clusters_list['clusters']:
    if(item['cluster_name'] == cluster_name):
        exists = True
        solr_cluster = item
        break
if(exists):
    print(json.dumps(solr_cluster, indent=2))
    print('Cluster exists')
    solr_cluster_id = solr_cluster['solr_cluster_id']
else:
    print('Cluster does not exist')
    sys.exit()
#%%
configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
print(json.dumps(configs, indent=2))
#%%
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
print(json.dumps(collections, indent=2))

#%%
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'AI')
results = pysolr_client.search("j.app.mech. 3,1947, a269.")
print('{0} documents found'.format(len(results.docs)))
for item in results.docs:
    print(item['id'])
