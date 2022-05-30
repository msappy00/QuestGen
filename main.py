import nltk
from pprint import pprint
from Questgen import main
nltk.download('stopwords')

payload = {
            "input_text": """ \
One day, the Virgin Mary appeared to a woodcutter in the forest. \
She said, ‘You are poor and needy. Bring me your little girl, and I will care for her. \
The woodcutter obeyed, and the Virgin Mary took the child to heaven. \
The girl lived a good life and grew strong. \
When she turned 14, the Virgin Mary called for her. \
She told the girl, ‘I’ll be away for a while. \
You’ll be responsible for these keys to the 13 doors of heaven. \
“You can open all except the 13th door. \
However, the girl was curious and didn’t obey. \
Some time later, the Virgin Mary returned. \
When she asked about the 13th door, the girl lied about not opening it. \
So the Virgin Mary took her voice and sent her away. \
The girl ended up in a forest on Earth. \
She stayed there for many years. \
Then, the king of the land found her. \
He thought that she was very beautiful and invited her to his castle. \
Since the girl couldn’t speak, she just nodded her head a little. \
"""
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

pprint(output)
