#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:10:00 2017

@author: soren
"""

import json
#from watson_developer_cloud import RetrieveAndRankV1
from source.rr.ConfuciusRR import ConfuciusRetrieveAndRankV1
#%%

with open('resources/config/rr-config.json') as rr_config:
    config = json.load(rr_config)
retrieve_and_rank = ConfuciusRetrieveAndRankV1(
    username = config['credentials']['username'],
    password= config['credentials']['password'])

solr_cluster_id = 'scc3ecccbb_2901_4275_b4d7_11342899dca1'
ranker_id = '1eec74x28-rank-5332'
results = retrieve_and_rank.rank(solr_cluster_id, ranker_id, 'reddit_data', 'Why is the sun hotre?')
