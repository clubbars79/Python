word = str.upper(input())
points = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ',
          4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
letter = [key for i in word for key, value in points.items() if i in value]
print('Количество очков в слове ', word, sum(letter))
