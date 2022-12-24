'''def fname(a):
    i=0
    s=0
    while a>=i:
        s+=i
        i+=1
    return(s)
print(fname(int(input('enter the number'))))
'''
'''def sam(a):
    if a%2==0:
        return True
    return False
print(sam(12))
'''
def lugg(a,sw=25,b=500,c=0):
    for i in a:
        if i<=sw:
            c+=b
        else:
            c+=b*2
    print(c)
lugg(eval(input('enter the list')))
