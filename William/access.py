import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='1a0b77b6-b49b-48cb-866a-0077f016a506',
  password='v88OuvDlfLcQ')

#classifiers = natural_language_classifier.list()
#print(json.dumps(classifiers, indent=2))

question = input('State your question: ')
#status = natural_language_classifier.status('cedf17x168-nlc-108')
classes = natural_language_classifier.classify('cedf17x168-nlc-108', question)
print(json.dumps(classes, indent=2))
