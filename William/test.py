import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='1a0b77b6-b49b-48cb-866a-0077f016a506',
  password='v88OuvDlfLcQ')

with open('../Tyler/trainingData_Tyler.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='My Classfier',
    language='en'
  )
print(json.dumps(classifier, indent=2))
