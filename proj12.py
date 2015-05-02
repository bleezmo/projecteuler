def getTriangle(x):
    num = 1
    for i in range(2,x+1):
        num = num + i
    return num

def getDivisors(n):
    plist = []
    for f in getFactors(n):
        foundMatch = False
        for pair in plist:
            if pair[0] == f:
                foundMatch = True
                pair[1] = pair[1] + 1
        if not foundMatch:
            plist = plist + [[f,1]]
    result = 1
    for pair in plist:
        result = result * (pair[1]+1)
    return result

def getFactors(n):
    for i in range(2,n):
        if n%i == 0:
            return getFactors(i) + getFactors(n//i)
    return [n]

def checkNumber(count):
    triangle = getTriangle(count)
    result = getDivisors(triangle)
    return (result>500,triangle)

def main():
    i = 0
    while True:
        i+=1
        result = checkNumber(i)
        if result[0]:
            print("found it:",result[1])
            break

main()
