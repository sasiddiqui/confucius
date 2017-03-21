ROOT=../..
DATASET=history
python2.7 $ROOT/source/data-process/processPosts.py $ROOT/resources/data/$DATASET/$DATASET.xml

DATASET=astronomy
python2.7 $ROOT/source/data-process/processPosts.py $ROOT/resources/data/$DATASET/$DATASET.xml

DATASET=music
python2.7 $ROOT/source/data-process/processPosts.py $ROOT/resources/data/$DATASET/$DATASET.xml

DATASET=ai
python2.7 $ROOT/source/data-process/processPosts.py $ROOT/resources/data/$DATASET/$DATASET.xml

DATASET=cooking
python2.7 $ROOT/source/data-process/processPosts.py $ROOT/resources/data/$DATASET/$DATASET.xml
