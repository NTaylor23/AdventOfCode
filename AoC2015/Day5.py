
def bannedWords(word):
    banned = ['ab', 'cd', 'pq', 'xy']
    return not any(ban in word for ban in banned)


def vowelCount(word):
    vowels = 'aeiou'
    count = 0
    for char in vowels:
        count += word.count(char)
    return count >= 3


# can be more efficient?
def repeatChar(word, spacing):
    for i in range(0, len(word) - spacing):
        if word[i] == word[i + spacing]:
            return True
    return False


def repeatPair(word):
    for i in range(0, len(word)):
        currentPair = word[i:i+2]
        if currentPair in word[i+2:]:
            return True
    return False


def day5():
    nice = 0
    with open('day5input', 'r') as words:
        for line in words:
            if repeatPair(line) and repeatChar(line, 2):
                nice += 1
    print(nice)


day5()
