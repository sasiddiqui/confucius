import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='74173aac-8171-4054-b2db-fa873012069e',
  password='OKwSvr3BdvKc')

#
# #  CLASSIFIER CREATION:
# with open('PostsAI.xml.nlc.csv', 'rb') as training_data:
#   classifier = natural_language_classifier.create(
#     training_data=training_data,
#     name='ai2',
#     language='en'
#   )
# print(json.dumps(classifier, indent=2))


#CHECK THE STATUS of the classifier
status = natural_language_classifier.status('f5b42ex171-nlc-3644')
print (json.dumps(status, indent=2))


# #DELETE CLASSIFIERS
# natural_language_classifier.remove('f5bbbbx174-nlc-2406')
# natural_language_classifier.remove('f5b42ex171-nlc-2397')
# natural_language_classifier.remove('cedd09x164-nlc-83')


#LIST CLASSIFIERS
# classifiers = natural_language_classifier.list()
# print(json.dumps(classifiers, indent=2))


#ACTUALLY CLASSIFY INTO A CLASS
def classify(id, question):
    classes = natural_language_classifier.classify(id, question)
    #print(classes)
    j = json.loads(json.dumps(classes))
    class_name = j['top_class']
    return class_name

question = raw_input('ask your question: ')


print (classify('f5b42ex171-nlc-3644', question))