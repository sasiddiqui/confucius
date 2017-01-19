import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='c438a647f6f19338fd3ad5c7c74f759fa40bcc0e')

print(json.dumps(visual_recognition.detect_faces(images_url='https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'), indent=2))

