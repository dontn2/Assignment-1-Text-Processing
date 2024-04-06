def tokenize(textFilePath) -> list:
    """
    Runtime Complexity:
    """
    tokenList = []
    token = ""
    with open(textFilePath) as text:
        while True:
            char = text.read(1)
            if char.isalnum():
                token = token + char.lower()
            else:
                tokenList.append(token)
                token = ""
                if char == "":
                    break
    return tokenList


def computeWordFrequencies(tokenList) -> dict:
    """
    Runtime Complexity:
    """
    tokenCount = {}
    for token in tokenList:
        if token in tokenCount:
            tokenCount[token] += 1 
        else:
            tokenCount[token] = 1
    return tokenCount

def printFrequencies(tokenCount) -> None:
    """
    Runtime Complexity:
    """
    orderedCount = sorted(tokenCount.items(), key=lambda pair: pair[1], reverse=True)
    for pair in orderedCount:
        print(pair[0] + " " + str(pair[1]))

if __name__ == "__main__":
    tokenList = tokenize("text3.txt")
    tokenCount = computeWordFrequencies(tokenList)
    printFrequencies(tokenCount)
