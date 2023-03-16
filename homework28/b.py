def search(lexicon, target):
    return _search(lexicon,target,0,len(target))
def _search(lexicon,target,a,b):
    if (a)>=(b):
        return b
    else:
        c =((a+b)//2)
        if (target==lexicon[c]):
            return c
        elif (target)<(lexicon[c]):
            return _search(lexicon,target,a,c)
        elif (target)>(lexicon[c]):
            return _search(lexicon,target,c+1,b)
