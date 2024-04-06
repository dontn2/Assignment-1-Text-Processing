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

def printFrequencies(tokenCount) -> None:
    """
    Runtime Complexity:
    """

if __name__ == "__main__":
    tokenList = tokenize("text1.txt")
    for token in tokenList:
        print(token)
