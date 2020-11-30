string = ''
with open('statements.txt','r') as file:
    for _ in file:
        line = _.lower().replace('.', ' ').replace(',', ' ').replace("ï¿½", '')\
            .replace('\n', ' ').replace('?', ' ')
        string += line

data = string.split()
dict = {}
for i in set(data):
    dict[i] = data.count(i)
print(dict)
print(sorted(dict.items(), key=lambda x: x[1], reverse=True))
