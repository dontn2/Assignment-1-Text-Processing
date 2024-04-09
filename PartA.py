def tokenize(textFilePath) -> list:
    """
    Runtime Complexity: O(n) since it's going through every character once to check if it should be added to a token so the function
    grows linearly with the size of the text file
    """
    tokenList = []
    token = ""
    with open(textFilePath) as text:
        while True:
            char = text.read(1)
            if isalphanumeric(char):
                token = token + char.lower()
            else:
                if not token == "":
                    tokenList.append(token)
                token = ""
                if char == "":
                    break
    return tokenList


def computeWordFrequencies(tokenList) -> dict:
    """
    Runtime Complexity: O(n) since it's going through every token and increasing the counter. 
    The function grows linearly with the number of tokens
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
    Runtime Complexity: O(n) since it's 
    """
    orderedCount = sorted(tokenCount.items(), key=lambda pair: pair[1], reverse=True)
    for pair in orderedCount:
        print(pair[0] + "-" + str(pair[1]))

def isalphanumeric(char) -> bool:
    """
    Runtime complexity:
    """
    if char.lower() in f'abcdefghijklmnopqrstuvwxyz1234567890':
        if char.lower() == "":
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    tokenList = tokenize("canvas2.txt")
    tokenCount = computeWordFrequencies(tokenList)
    printFrequencies(tokenCount)
    # TODO Add runtime Complexity
    # TODO remove test code