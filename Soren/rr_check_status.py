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
#List all clusters
cluster_name = config['solr_cluster_name']
solr_clusters_list = retrieve_and_rank.list_solr_clusters()
print(json.dumps(solr_clusters_list, indent=2))
#%%
solr_cluster_id = "sc5352d79e_c165_44a6_97ca_8384501d30dd"
#%%
#Delete a cluster

#%%
#List all configs
configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
print(json.dumps(configs, indent=2))
#%%
#Delete a Config

#%%
#List all collections
collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
print(json.dumps(collections, indent=2))
#%%
#Delete a collections

#%%
#Query using basic Retrive
pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'AI')
results = pysolr_client.search("*")
print('{0} documents found'.format(len(results.docs)))
for item in results.docs:
    print(item['id'])
#%%
#Add a document to Solr

#%%
#List all rankers
rankers = retrieve_and_rank.list_rankers()
print(json.dumps(rankers, indent=2))
#%%
#Create a Ranker

#%%
#Query using Ranker
ranker_id = ""
ranker_results = retrieve_and_rank.rank(ranker_id, "query")
print(json.dumps(ranker_results, indent=2))
#%%
#