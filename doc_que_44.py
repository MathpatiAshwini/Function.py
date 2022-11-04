
def sample():
    a=['a',1, '2', 5, 'b', 'q']
    i=0
    while i<len(a):
        if i==2:
            print(a[-1:-3:-1])
        if i==3:
            print(a[-1:-4:-1])
        i+=1
sample()

