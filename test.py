# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    #uses a tree structure to see what is next in the pattern. each value has 2 branches, one for myltiplying the previous element by 2 and one for increasing it by 1. If one branch results in a value already found, that branch is not expanded farther. If a value is found that is above N, it is not expanded farther


    nodesVisited = [1]#starts with the first step. Filled with values that have already been tried
    nodesToExpand = [1]
    newNodesToExpand = []

    if N == 1:#base case
        return 1

    steps = 1

    while True:
        steps += 1

        for x in nodesToExpand:
            #if value has been found before do not add it to values to be expanded later
            if x*2 not in nodesVisited and x*2 <= N:
                newNodesToExpand.append(x*2)
            if x+1 not in nodesVisited and x+1 <= N:
                newNodesToExpand.append(x+1)

        if N in newNodesToExpand:#solution Found
            break

        #moves to new list of values to expand
        nodesVisited += nodesToExpand
        nodesToExpand = newNodesToExpand.copy()
        newNodesToExpand = []
            


    # write your code in Python 3.6

    return steps
    pass
