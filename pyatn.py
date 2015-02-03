import random

def printPath(finalState, finalState1, initState, parent):
    if finalState in parent:
        current = finalState
    else:
        current = finalState1 
    print 'path:'
    while current in parent and not current == initState:
        print current
        current = parent[current]
    print current

def stepUp(state):
    l=[a for a in state]
    ind=l.index(0)
    if ind in [0,1,2]:
        return state
    l[ind]=l[ind-3]
    l[ind-3]=0
    return tuple(l)

def stepDown(state):
    l=[a for a in state]
    ind=l.index(0)
    if ind in [6,7,8]:
        return state
    l[ind]=l[ind+3]
    l[ind+3]=0
    return tuple(l)

def stepLeft(state):
    l=[a for a in state]
    ind=l.index(0)
    if ind in [0,3,6]:
        return state
    l[ind]=l[ind-1]
    l[ind-1]=0
    return tuple(l)

def stepRight(state):
    l=[a for a in state]
    ind=l.index(0)
    if ind in [2,5,8]:
        return state
    l[ind]=l[ind+1]
    l[ind+1]=0
    return tuple(l)

def nextFront(front, parent):
    result=[]
    for st in front:
        up=stepUp(st)
        if up not in parent:
            result.append(up)
            parent[up]=st
        down=stepDown(st)
        if down not in parent:
            result.append(down)
            parent[down]=st
        left=stepLeft(st)
        if left not in parent:
            result.append(left)
            parent[left]=st
        right=stepRight(st)
        if right not in parent:
            result.append(right)
            parent[right]=st
    return result
    
    
def index(state,a):
    for i in range(len(state)):
        if (state[i]==a):
            return i
    return -1

def init(finalState):
    l = [a for a in finalState]
    random.shuffle(l)
    return tuple(l)

if __name__ == '__main__':
    finalState=(1,2,3,4,5,6,7,8,0)
    finalState1=(1,2,3,4,5,6,8,7,0)
    initState = init(finalState)
    print 'initial state:'
    print initState
    
    front=[initState]
    parent={}
    while not (finalState in front or finalState1 in front or len(front)==0):
        front=nextFront(front,parent)
        print 'states visited:' + str(len(parent))
        
    if len(front)==0:
        print 'no path found'
    else:    
        printPath(finalState, finalState1, initState, parent)