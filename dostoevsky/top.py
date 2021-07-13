key = []
key_sep = []
out = open('prepared_data.py', 'w', encoding='utf8')
res = []
a = open('topic_data1.txt', encoding='utf8').read().split('\'')
for i in a:
    if a.index(i) % 2 != 0:
        key.append(i)
for s in key:
    key_sep.append(s.split(' + '))
for e in key_sep:
    for g in e:
        res.append(g.split('*')[1].replace('"', ''))
print('from top', res)
print(res, file=out)
x =7
