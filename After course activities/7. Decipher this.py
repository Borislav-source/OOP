message = input().split()
result = []

for word in message:
    number = ''
    for char in word:
        if char.isdigit():
            number += char
    first_letter = chr(int(number))
    word = list(word[len(number):])
    word[0], word[-1] = word[-1], word[0]
    word.insert(0, first_letter)
    result.append(''.join(word))
print(' '.join(result))

