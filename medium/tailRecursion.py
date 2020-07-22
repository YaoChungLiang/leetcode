import time
def fact_tail(n, a = 1): 
  
    if (n == 0): 
        return a 
  
    return fact_tail(n - 1, n * a) 

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def fact_multi(n):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
    return tmp

if __name__ == "__main__":
    
    
    #fact(4)
    '''
    stack frames:
        fact(4)
        4*fact(3)
        4*(3*fact(2))
        4*(3*(2*fact(1)))
        4*(3*(2*(1*fact(0))))
        4*(3*(2*(1*1)))
        4*(3*(2*1))
        4*(3*2)
        4*6
        24
    '''
    #fact_tail(4)
    '''
    stack frames:
        fact(4,1)
        fact(3,4*1)
        fact(2,3*4*1)
        fact(1,2*3*4*1)
        fact(0,1*2*3*4*1)
        24
    '''
    print(fact_multi(4))