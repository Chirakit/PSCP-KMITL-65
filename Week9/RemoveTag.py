'''RemoveTag'''
def tag():
    '''_'''
    message = input().replace("<", "$<").replace(">", ">$").split("$")
    check = list(filter(lambda x, ok="<": ok not in x, message))
    value = ' '.join(check)
    print(value.split())
tag()
