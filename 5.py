a=input()
#LLBLRRBRL
c = ''
d = ''
g = ''
x = []
for i in a:
    if i==c:
        continue
    if i!=c:
        d+=i
    c=i
for i in range(d.count('B')):
    if d[0]=='B':
        g+=d[0]
        d=d[1::]
    if d[d.index('B')-1]==d[d.index('B')+1]:
        d=d[:d.index('B')+1]+d[d.index('B')+2:]
        g+=d[:d.index('B')]
        d=d[d.index('B'):]


        
        
        
    
print(len(d)+len(g))
    

    
    
