def abc(*args):
    if len(args) == 0:
        return None
    max = args[0]
    for i in args:
        if max<i:
            max = i
    return max
def bcd(*args):
    if len(args) == 0:
        return None
    max = args[0]
    for i in args:
        if len(max)<len(i):
            max = i
    return max
print(abc(10,20,30,40,50))
print(bcd("Ayush","Laxmikant Aiyyar","Raj","Raghu","Krishna"))
