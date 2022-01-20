import math
global tol
def func(x):
    return (A*math.exp(a*x))+(B*x)+C
def derivative(x):
    return (A*a*math.exp(a*x))+B
def solve(pole,d):
    x=pole
    jump=10
    while True: 
        a=x
        x+=(jump*d)
        if func(x)*func(a)<=0:
            if func(x)==0 or (func(x)>0 and jump<tol):
                break
            jump/=10
            d*=-1
    return x
print("Solving Transcendental equation of form A(e^ax)+ Bx + C = 0")
print("Enter A, a, B and C values:")
A=int(input())
a=int(input())
B=int(input())
C=int(input())
if (a==0 or A==0) and B==0:
    print("Invalid input!")
else:
    if a==0 or A==0:
        print("The given equation has a single root")
        print("x = ",-(A+C)/B)
    else:
        if -B/(A*a)>0:
            c=(math.log(-B/(A*a)))/a
            if A*func(c)*math.exp(a*c)>0:
                print("The given equation has no root!")
            else:
                tol=float(input("Enter tolerance value in powers of 10 (-ve):"))
                tol=pow(10,tol)
                print("The given equation has two roots")
                print("x1 = ",solve(c,1))
                print("x2 = ",solve(c,-1))
        else:
            if B==0 and A*C>=0:
                print("The given equation has no root!")
            else:
                if A+C!=0:
                    tol=float(input("Enter tolerance value in powers of 10 (-ve):"))
                    tol=pow(10,tol)
                print("The given equation has a single root")
                if A+C==0:
                    print("x =  0")
                else:
                    d=1 if (A*a+B)*(A+C)<0 else -1
                    print("x = ",solve(0,d))
        
        
            
    
    
    




