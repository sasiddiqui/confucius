import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='74173aac-8171-4054-b2db-fa873012069e',
  password='OKwSvr3BdvKc')


##  CLASSIFIER CREATION:
# with open('NLCtrain.csv', 'rb') as training_data:
#   classifier = natural_language_classifier.create(
#     training_data=training_data,
#     name='My Classfier',
#     language='en'
#   )
# print(json.dumps(classifier, indent=2))


## CHECK THE STATUS of the classifier
status = natural_language_classifier.status('f5bbbcx175-nlc-1013')
print (json.dumps(status, indent=2))


#DELETE CLASSIFIERS
# natural_language_classifier.remove('ff18a8x156-nlc-4861')
# natural_language_classifier.remove('cede31x166-nlc-111')
# natural_language_classifier.remove('cedd09x164-nlc-83')


#LIST CLASSIFIERS
classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))


# #ACTUALLY CLASSIFY INTO A CLASS
# def classify(id, question):
#   classes = natural_language_classifier.classify(id, question)
#   print(json.dumps(classes, indent=2))

