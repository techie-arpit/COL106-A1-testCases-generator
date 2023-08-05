import sys;
sets=[set() for i in range(0,100001)]
def process(line):
    p=list(map(int,line.split(" ")))
    if p[0]==1:
        sets[p[1]].add(p[2])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==2:
        sets[p[1]].discard(p[2])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==3:
        if p[2] in sets[p[1]]:
            print(1)
        else:
            print(0)
        pass
    elif p[0]==4:
        sets[p[1]].update(sets[p[2]])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==5:
        sets[p[1]].intersection_update(sets[p[2]])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==6:
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==7:
        sets[p[1]].difference_update(sets[p[2]])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==8:
        sets[p[1]].symmetric_difference_update(sets[p[2]])
        print(len(sets[p[1]])+0)
        pass
    elif p[0]==9:
        print(",".join([str(i) for i in sorted(sets[p[1]])]))
        pass

while True:
    try:
        line =input()
        process(line)
    except EOFError:
        break