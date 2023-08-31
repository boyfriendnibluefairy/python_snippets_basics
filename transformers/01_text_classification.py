##
##  Classify two sentences whether they are
##  contradiction, neutral, entailment
##  by Hugging Face
##
from transformers import pipeline   ## pip install transformers

## List of Tasks
## huggingface.co/tasks

## List of Models
## huggingface.co/models

specific_model = "distilbert-base-uncased-finetuned-sst-2-english"
specific_task = "text-classification"
classifier = pipeline(task=specific_task, model=specific_model)

## test the classifier
# result1 = classifier([
#     "I love you.",
#     "I hate you.",
#     "Gilas Pilipinas coach is Chot Reyes",
#     "Gilas Pilipinas coach is Tab Baldwin"
# ])
## print(result1)
## OUTPUT:
## [{'label': 'POSITIVE', 'score': 0.9998705387115479},
# {'label': 'NEGATIVE', 'score': 0.9992952346801758},
# {'label': 'POSITIVE', 'score': 0.9931597709655762},
# {'label': 'POSITIVE', 'score': 0.9635142087936401}]



result2 = classifier([
    "I am from the Philippines",
    "I am from the Japan",
    "I am from the China",
    "I am from the USA",
    "I am from Russia",
    "I am from India",
    "I am from Ukraine"
])
print(result2)
## OUTPUT:
## [{'label': 'POSITIVE', 'score': 0.9909703731536865},
# {'label': 'POSITIVE', 'score': 0.9831674695014954},
# {'label': 'POSITIVE', 'score': 0.9763003587722778},
# {'label': 'POSITIVE', 'score': 0.9642282128334045},
# {'label': 'POSITIVE', 'score': 0.9924020767211914},
# {'label': 'POSITIVE', 'score': 0.9907897710800171},
# {'label': 'POSITIVE', 'score': 0.9925392270088196}]


