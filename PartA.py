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
    for token in tokenCount:
        print(token + " " + str(tokenCount[token]))

if __name__ == "__main__":
    tokenList = tokenize("text1.txt")
    tokenCount = computeWordFrequencies(tokenList)
    printFrequencies(tokenCount)
