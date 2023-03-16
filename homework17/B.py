def setDefaultValue(data,key,value):
    if key in data:
        insert=data[key]
        return insert
    else:
        insert=value
        return value

