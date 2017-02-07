#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check the information about the Retrive and Rank Service

Created on Tue Feb  7 16:07:57 2017

@author: soren
"""
#%%
import json
from watson_developer_cloud import RetrieveAndRankV1
credentials_string = '''{
  "url": "https://gateway.watsonplatform.net/retrieve-and-rank/api",
  "password": "ANlCCDTtOHr4",
  "username": "55729e6b-2d18-46f8-b6a0-3e87cdd80797"
}'''
credentials = json.loads(credentials_string)
retrieve_and_rank = RetrieveAndRankV1(
    username = credentials['username'],
    password= credentials['password'])
#%%

solr_clusters = retrieve_and_rank.list_solr_clusters()
print(json.dumps(solr_clusters, indent=2))
solr_cluster_id = 'sc00f69555_6065_4fac_81d9_6d73bec5d006'
status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
#%%
configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
print(json.dumps(configs, indent=2))