#!/bin/bash
ROOT=./
DATASET=reddit_data
INPUT_DATA=$ROOT/resources/data/$DATASET/training.csv
USERNAME=55729e6b-2d18-46f8-b6a0-3e87cdd80797
PASSWORD=ANlCCDTtOHr4
CLUSTER_ID=scc3ecccbb_2901_4275_b4d7_11342899dca1
python2.7 $ROOT/source/rr/train.py -u $USERNAME:$PASSWORD -i $INPUT_DATA -c $CLUSTER_ID -x $DATASET -n $DATASET -d
