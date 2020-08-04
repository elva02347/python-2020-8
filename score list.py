listnames = ['chris','ivy','amy','jill','james','wendy','anna','iris']
listscore = [90,67,76,81,79,97,82,73]
'''
a = []
a.append(listnames) 
a.append(listscore)

print(listnames[1],listscore[1])

for i in range(5):
    score = int(input('fill in your score:'))
    if score not in listscore:
        listscore.append(score)
'''
sum_score = sum(listscore)
#print(listscore)
print('class average:',sum_score/8)

highest = 0
for n in listscore:
    if n > highest:
        highest = n

lowest = 100
for m in listscore:
    if m < lowest:
        lowest = m
        
for i in range(8):
    if highest == listscore[i]:
        print('class highest:',listnames[i],highest)
for j in range(8):
    if lowest == listscore[j]:
        print('class lowest:',listnames[j],lowest)

