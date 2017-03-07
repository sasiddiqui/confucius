#!/bin/bash
ROOT=../..
DATASET=ai
INPUT_DATA=$ROOT/resources/data/$DATASET/$DATASET.xml.ranker.csv
USERNAME=55729e6b-2d18-46f8-b6a0-3e87cdd80797
PASSWORD=ANlCCDTtOHr4
CLUSTER_ID=sc5352d79e_c165_44a6_97ca_8384501d30dd
python2.7 $ROOT/source/rr/train.py -u $USERNAME:$PASSWORD -i $INPUT_DATA -c $CLUSTER_ID -x $DATASET -n $DATASET -d > log.html
