temps =[100,223,345, -9999]
def foo(*args):
    print(type(args))
    args1 = (x.upper() for x in args)
    print(type(args1))
    
    args2 = [x.upper() for x in args]
    print(type(args2))
    return sorted(args)


new_temp=[temp/10 for temp in temps]
print(new_temp)

new_temp2 =[temp/10 for temp in temps  if temp !=-9999] 
print(new_temp2)

print(foo("deba","abs"))

