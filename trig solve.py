import math as m
global tol
global roots
roots=[]
def func(x):
    return (A*m.cos(a*x))+(B*m.sin(a*x))+(C*x)+D
def derivative(x):
    return (-A*a*m.sin(a*x))+(B*a*m.cos(a*x))+C
def ext(n):
    x0=(n*m.pi/a)+(pow(-1,n)*a1)-a2 if abs(a1)!=m.pi/(2*a) else (((4*n+1)*m.pi/2 if a1<0 else (4*n+3)*m.pi/2)-a2)
    return x0
def solve(pole,d,jump=10):
    x=pole
    while True: 
        a=x
        x+=(jump*d)
        if func(x)*func(a)<=0:
            if func(x)==0 or (func(x)>0 and jump<tol):
                break
            jump/=10
            d*=-1
    return x
def root(g):
    n=0
    while True:
        if func(ext(n))*func(ext(n+g))>0:
            if func(ext(n))*C*g<0:
                n+=g
            else:
                break
        else:
            if ext(n)*ext(n+g)<0 and A+D==0 and (0 not in roots):
                roots.append(0)
            else:
                j=abs(ext(n+g)-ext(n))
                r=solve(ext(n),g,j)
                roots.append(r)
            n+=g
print("Solving Trigonometric-Linear equation of form A(cos(ax)) + B(sin(ax)) + Cx + D = 0")
print("Enter A, a, B, C and D values:")
A=int(input())
a=int(input())
B=int(input())
C=int(input())
D=int(input())
if a<0:
    a*=-1
    B*=-1
if A==0 and B==0:
    if C==0:
        print("Invalid input!")
    else:
        print("The given equation has a single root")
        print("x = ",-D/C)
elif a==0:
    if C==0:
        print("Invalid input!")
    else:
        print("The given equation has a single root")
        print("x = ",-(B+D)/C)
else:
    if C==0:
        if abs(D/m.sqrt(A*A+B*B))<=1:
            if A==0:
                a1=m.asin(-D/B)/a
                a2=0
            elif B==0:
                a1=m.asin(-D/A)/a
                a2=m.pi/(2*a)
            else:
                a1=m.asin(-D/m.sqrt(A*A+B*B))/a
                a2=m.atan(A/B)/a
                if B<0:
                    a1*=-1
            print("The given equation has infinite number of solutions!")
            s1="+ ((-1)^n)( "+str(a1)+" )" if a1!=0 else ''
            s2=(" + ( "+str(-a2)+" )" if a2!=0 else '')+", n is an integer"
            print("\nGeneral form: x = n( "+str(m.pi/a)+" )"+s1+s2)
        else:
            print("The given equation has no root!")
    else:
        amp=a*m.sqrt(A*A+B*B)
        tol=float(input("Enter tolerance value in powers of 10 (-ve):"))
        tol=pow(10,tol)
        if abs(C/amp)>=1:
            print("The given equation has a single solution!")
            d=1 if C*(A+D)<0 else -1
            print("x = ",solve(0,d))
        else:
            if B==0:
                a1=m.asin(C/(A*a))
                a2=0
            elif A==0:
                a1=m.asin(-C/(B*a))
                a2=m.pi/(2*a)
            else:
                a1=m.asin(-C/amp)/a
                a2=m.atan(-B/A)/a
                if A>0:
                    a1*=-1
            root(1)
            root(-1)
            roots.sort()
            print("The given equation has",len(roots),"root{}!".format('s' if len(roots)>1 else ''))
            i=1
            for r in roots:
                print("x{}  =  {}".format(i,r))
                i+=1
            

                  
                
                
            
            
        
        
            
