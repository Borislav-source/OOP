collection = input().split(', ')
data = input()

while not data == 'Craft!':
    command, item = data.split(' - ')
    if command == 'Collect':
        if item not in collection:
            collection.append(item)
    elif command == 'Drop':
        if item in collection:
            collection.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in collection:
            index = collection.index(old_item)
            collection.insert(index+1, new_item)
    elif command == 'Renew':
        if item in collection:
            collection.remove(item)
            collection.append(item)
    data = input()
print(', '.join(collection))
