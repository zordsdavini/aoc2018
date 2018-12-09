f = open('input.txt', 'r')
row = f.read()
data = row.split()

print('Building node tree...')
children = {0: 1}
metadata = {}
deep = 1
slot = 2
nodes = {}
parent = 0
node = 0
node_counter = 0
for i in data:
    i = int(i)
    if slot == 2 and children[deep - 1] > 0 and (deep not in metadata or metadata[deep] == 0):
        children[deep] = i
        children[deep - 1] -= 1
        slot = 1

        node_counter += 1
        node = node_counter
        info = {
                'parent': parent,
                'deep': deep,
                'metadata': [],
                'children': [],
                'children_count': i
                }
        nodes[node] = info

        if parent in nodes:
            nodes[parent]['children'].append(node)
        continue
    if slot == 2 and deep in children and children[deep] == 0 and deep in metadata and metadata[deep] > 0:
        metadata[deep] -= 1

        nodes[node]['metadata'].append(i)

        if metadata[deep] == 0 and children[deep - 1] == 0:
            while deep in metadata and metadata[deep] == 0:
                deep -= 1

                node = parent
                if parent in nodes:
                    parent = nodes[parent]['parent']
                else:
                    parent = 0
        continue
    elif slot == 1:
        metadata[deep] = i
        slot = 2
        if children[deep] > 0:
            deep += 1

            parent = node

        nodes[node]['metadata_count'] = i
        continue


def count_metadatas(node):
    info = nodes[node]
    if info['children_count'] == 0:
        result = 0
        for m in info['metadata']:
            result += int(m)
        return result

    result = 0
    for m in info['metadata']:
        mi = m - 1
        if mi < info['children_count']:
            result += count_metadatas(info['children'][mi])

    return result


print('Counting metadatas...')
print('Result:', count_metadatas(1))
