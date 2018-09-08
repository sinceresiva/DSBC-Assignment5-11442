import pandas as pd

def getDistanceVector(dfX):
    indexOfZero=0
    currentIndex=0
    dfY = pd.DataFrame(columns=['Y'])
    increment=1
    while currentIndex<len(dfX['X']):
        item = dfX['X'][currentIndex]
        if item == 0:
            indexOfZero = currentIndex
            resultItem=item
            increment=0
        else:
            resultItem=currentIndex-indexOfZero+increment
        dfY['Y'].loc[currentIndex]=resultItem
        currentIndex+=1
    dfX['Y']=dfY['Y']

dfX=pd.DataFrame({'X':[7,2,0,3,4,6,0,4,5]})
#Result {'Y':[1,2,0,1,2,3,0,1,2]}
getDistanceVector(dfX)
print(dfX)

dfX=pd.DataFrame({'X':[4,0,1,0,7,6,0]})
#Result {'Y':[1,0,1,0,1,2,0]}
getDistanceVector(dfX)
print(dfX)

print('Done')