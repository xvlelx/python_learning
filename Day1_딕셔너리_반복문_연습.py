score = {'현기' : 85, '철수':90,'영희':88}

for name in score:
    print(name)
for scores in score.values():
    print(scores)
for name,scores in score.items():
    print(name, scores)