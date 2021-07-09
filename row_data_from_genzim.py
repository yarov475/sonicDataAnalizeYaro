out = open('prepared_data_for_Dost.txt', 'w', encoding='utf8')
res = []
a = [(0,
      '0.004*"день" + 0.004*"дома" + 0.004*"это" + 0.003*"наши" + 0.003*"немцы" + 0.003*"воиска" + 0.003*"сад" + 0.003*"города" + 0.003*"воина" + 0.003*"ребята"')]
arr = a[0][1].split(' + ')
for s in arr:
    sArr = (s.split('*'))
    for i in sArr:
        if sArr.index(i)%2 != 0:
            res.append(i.replace('"', ''))

print(res, file=out)
