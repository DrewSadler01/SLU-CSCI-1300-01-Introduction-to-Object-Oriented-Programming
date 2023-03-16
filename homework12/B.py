def isSubstring(pattern, original):
    for a in range(len(original)-len(pattern)+1):
        checker = True
        for b in range(len(pattern)):
            if pattern[b] != original[b+a]:
                checker = False	
                break
	if checker:
            return True
    return False
