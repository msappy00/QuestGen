# import nltk
# from pprint import pprint
from Questgen import main
# nltk.download('stopwords')

payload = {
            "input_text": "For a Python dictionary, you can get the value of a key using the [] notation. "
}
# True / False
# qe = main.BoolQGen()
# output = qe.predict_boolq(payload)

# Multiple Choice Questions
qg = main.QGen()
output = qg.predict_shortq(payload)

# FAQs
# output = qg.predict_shortq(payload)
# pprint (output)

for i in range(0, len(output["questions"])):
    print()
    print(output["questions"][i]["Question"])
    print("Answer: {}".format(output["questions"][i]["Answer"]))
