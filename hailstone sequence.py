import matplotlib.pyplot as plt


def GetWidth(a, b):
    return (a+b)/2


def solution(k, ranges):
    sqc = []
    answer = k
    sqc.append(k)
    
    while answer!=1:
        if answer %2==0:
            answer /=2
        else :
            answer = answer*3+1
            
        sqc.append(answer)
    
    print(sqc)

    plt.plot(sqc)
    plt.show()
    
    answer = 0
    
    if sum(ranges)>0:
        for i in range(ranges[0], ranges[-1]): 
            answer += GetWidth(sqc[+i], sqc[+i+1])
    else:
        for i in range(0, len(sqc)-1):
            answer += GetWidth(sqc[+i], sqc[+i+1])
    
    return answer




print(solution(5, [0,0]))





