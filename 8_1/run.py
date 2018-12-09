f = open('input.txt', 'r')
row = f.read()
data = row.split()

result = 0
children = {0: 1}
metadata = {}
deep = 1
slot = 2
for i in data:
    i = int(i)
    if slot == 2 and children[deep - 1] > 0 and (deep not in metadata or metadata[deep] == 0):
        children[deep] = i
        children[deep - 1] -= 1
        slot = 1
        continue
    if slot == 2 and deep in children and children[deep] == 0 and deep in metadata and metadata[deep] > 0:
        result += i
        metadata[deep] -= 1
        if metadata[deep] == 0 and children[deep - 1] == 0:
            while deep in metadata and metadata[deep] == 0:
                deep -= 1
        continue
    elif slot == 1:
        metadata[deep] = i
        slot = 2
        if children[deep] > 0:
            deep += 1
        continue

print('Result:', result)
