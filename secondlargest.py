import sys
def secondlargest(input):
    first=second=sys.maxsize
    for i in input:
        if(first > i):
            second=first
            first=i
    print(second)

input=[2,32,1,5,4]
secondlargest(input)