out = open('prepared_data_for_Dost.txt', 'w', encoding='utf8')
res = []
strings = []
arrS = []
s = ''
a =     [(0,
      '0.004*"молотов" + 0.004*"день" + 0.004*"немцы" + 0.004*"дома" + 0.003*"радио" + 0.003*"очень" + 0.003*"воиска" + 0.003*"воина" + 0.003*"наши" + 0.003*"города"'),
     (1,
      '0.005*"это" + 0.004*"день" + 0.004*"дома" + 0.004*"наши" + 0.003*"немцы" + 0.003*"воиска" + 0.003*"сад" + 0.003*"города" + 0.003*"ребята" + 0.003*"саду"'),
     (2,
      '0.004*"дома" + 0.004*"нам" + 0.003*"день" + 0.003*"наши" + 0.003*"это" + 0.003*"немцы" + 0.003*"взяли" + 0.003*"весь" + 0.003*"воиска" + 0.002*"свои"')]
for topics in a:
    strings.append(topics[1].split(' + '))
for arr in strings:
    for i in arr:
        arrS.append(i.split('*'))

for i in arrS:
    res.append(i[1].replace('"', ''))

print(res, file=out)
