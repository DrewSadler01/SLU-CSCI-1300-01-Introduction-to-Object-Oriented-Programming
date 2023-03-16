def letterFrequency(word):
    wordCount={}
    for letter in word:
        (wordCount[letter])=((wordCount.get(letter,0))+(1))
    return (wordCount)
