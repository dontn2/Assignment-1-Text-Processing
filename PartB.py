import PartA

def countCommonTokens(file1Tokens, file2Tokens) -> int:
    count = 0
    file1Tokens = removeDuplicates(file1Tokens)
    for token in file1Tokens:
        if token in file2Tokens:
            count += 1
    return count

def removeDuplicates(givenList):
    result = []
    for element in givenList:
        if element not in result:
            result.append(element)
    return result 
    

if __name__ == "__main__":
    tokenList1 = PartA.tokenize("canvas1.txt")
    tokenList2 = PartA.tokenize("canvas2.txt")
    print(countCommonTokens(tokenList1, tokenList2))
    # TODO Add runtime Complexity
    # TODO remove test code