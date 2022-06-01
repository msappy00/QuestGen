from sense2vec import Sense2Vec
s2v = Sense2Vec().from_disk("s2v_old")

text = "dog"

if '|' not in text:
    parts = text.split('|')
    text = parts[0]
    text = s2v.get_best_sense(text)
    print("best guess: {}", format(text))

print()

most_similar = s2v.most_similar(text, n=4)

for similar in most_similar:
    print(similar)

other_senses = s2v.get_other_senses(text)
print(other_senses)
