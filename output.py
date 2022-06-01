output = {'questions': [{'Answer': 'powerhouse',
                         'Question': 'What is the mitochondria?',
                         'context': 'The mitochondria is the powerhouse of the cell.',
                         'id': 1},
                        {'Answer': 'mitochondria',
                         'Question': 'What is the powerhouse of the cell?',
                         'context': 'The mitochondria is the powerhouse of the cell.',
                         'id': 2}],
          'statement': 'The mitochondria is the powerhouse of the cell.'}

for i in range(0, len(output["questions"])):
    print()
    print(output["questions"][i]["Question"])
    print("Answer: {}".format(output["questions"][i]["Answer"]))
