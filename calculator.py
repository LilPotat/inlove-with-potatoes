a=input('enter the expression')
b=list(a)
def operation(x):
    global b
    for j in b:
            if not j.isalnum():
                m,n='',''
                if j==x:
                    d=1
                    while True:
                        try:
                            test=float(b[b.index(x)-d])
                            m+=b[b.index(x)-d]
                            d+=1                   
                            if d>b.index(x):
                                break
                        except ValueError:
                            break
                    if d>2:
                        m=m[::-1]
                    e=1
                    while True:
                        try:
                            try:
                                test=float(b[b.index(x)+e])
                                n+=b[b.index(x)+e]
                                e+=1
                            except ValueError:
                                break
                        except IndexError:
                            break
                    if x=='/':
                        c=float(m)/float(n)
                    elif x=='*':
                        c=float(m)*float(n)
                    elif x=='-':
                        c=float(m)-float(n)
                    elif x=='+':
                        c=float(m)+float(n)
                    l=b.index(x)
                    for i in range(b.index(x)-d+1,b.index(x)+e):
                        b[i]=str(c)
                    for i in range(d+e-2):
                        b.pop(l+e-1)
                        l-=1
def last(x):
    global b
    while True:
            operation(x)
            if x not in b:
                break
while True:
    if len(b)==1:
        break
    elif len(b)==0:
        print('bruh')
        break
    else:
        last('/')
        last('*')
        last('-')
        last('+')
        print(b[0])
                      
                                    
        
        
    
                    

                        
