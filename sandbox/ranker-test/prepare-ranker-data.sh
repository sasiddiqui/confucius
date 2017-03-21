#!/bin/bash
ROOT=../..
DATASET=cooking
INPUT_DATA=$ROOT/resources/data/$DATASET/$DATASET.xml.ranker.csv
USERNAME=55729e6b-2d18-46f8-b6a0-3e87cdd80797
PASSWORD=ANlCCDTtOHr4
CLUSTER_ID=sc0cbccce5_6f9c_41fa_86c5_1532f6a45e64
python2.7 $ROOT/source/rr/train.py -u $USERNAME:$PASSWORD -i $INPUT_DATA -c $CLUSTER_ID -x $DATASET -n $DATASET -d > ${DATASET}log.html
