def palindrome(word, index):
    if len(word) == 0 or len(word) == 1:
        return True

    if word[index] == word[index-1] and palindrome(word[1:-1], index):
        return f'{word} is a palindrome'
    return f"{word} is not a palindrome"


print(palindrome("petr", 0))
print(palindrome("aba", 0))
