import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='74173aac-8171-4054-b2db-fa873012069e',
  password='OKwSvr3BdvKc')


##  CLASSIFIER CREATION:
# with open('/Tyler/training_data.csv', 'rb') as training_data:
#   classifier = natural_language_classifier.create(
#     training_data=training_data,
#     name='My Classfier',
#     language='en'
#   )
#print(json.dumps(classifier, indent=2))


## CHECK THE STATUS of the classifier
status = natural_language_classifier.status('ff189ax155-nlc-4794')
print (json.dumps(status, indent=2))

# #ACTUALLY CLASSIFY INTO A CLASS
# def classify(id, question):
#   classes = natural_language_classifier.classify(id, question)
#   print(json.dumps(classes, indent=2))

