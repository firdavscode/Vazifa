def p(a,b,c,d):
    a,b = min(a,b),max(a,b)
    c,d = min(c,d),max(c,d)
    if b<c or d<a:
        return 0
    if a<=c<b<=d:
        return c,b
def yuza(a,b,c,d,e,f,g,h):
    ab = 0
    bc = 0
    cd = 0
    ad = 0
    ef = 0
    fg = 0
    gh = 0
    eh = 0
    for i in range(a,b):
        ab+=1
    for i in range(b,c):
        bc+=1
    for i in range(c,d):
        cd+=1
    for i in range(a,d):
        ad+=1




    for i in range(e,f):
        ef+=1
    for i in range(f,g):
        fg+=1
    for i in range(g,h):
        gh+=1
    for i in range(e,h):
        eh+=1
    print(ab,bc,cd,ad,ef,fg,gh,eh)

    if ab==gh and ad==fg:
        return ab*ad
    if b<=e and h<=d and c<=h and g<=d or b>=e and h>=d and c>=h and g>=d:
        if bc-fg==0 and cd-gh==0:
            return ad*ab    
    if d<e or h<b:
        return 0
    
        return (hg-cd)*(eh-bc)
a,b,c,d,e,f,g,h = map(int,input().split())
print(yuza(a,b,c,d,e,f,g,h))
