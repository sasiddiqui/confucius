#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:44:51 2017

@author: soren
"""

import json
from watson_developer_cloud import RetrieveAndRankV1

def retriveRank(question, topic):
    with open('credentials.json') as credentials_file:    
        credentials = json.load(credentials_file)
    retrieve_and_rank = RetrieveAndRankV1(
        username = credentials['username'],
        password= credentials['password'])
    # Replace with your own solr_cluster_id
    solr_cluster_id = 'scff1b48f6_5178_4c7c_bac8_39fffaf6f83f'
    
    pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, topic)
    # Can also refer to config by name
    
    #Example search
    results = pysolr_client.search(question)
    return results.docs[0]['body'][0]
    
retriveRank('semicolon', 'programming')