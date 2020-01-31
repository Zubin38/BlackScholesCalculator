#Zubin
from math import *

#(stock price current, exercise price, maturity in years, rate, volatility or sigma)
def d1(S,X,T,r,sigma):
    return (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))

def d2(S,X,T,r,sigma):
    return d1(S,X,T,r,sigma)-sigma*sqrt(T)

#define the call option price function
def bs_call(S,X,T,r,sigma):
    return S*CND(d1(S,X,T,r,sigma))-X*exp(-r*T)*CND(d2(S,X,T,r,sigma))

#define the put options price function
def bs_put(S,X,T,r,sigma):
    return X*exp(-r*T)-S + bs_call(S,X,T,r,sigma)

#define cumulative standard normal distribution
def CND(X):
     (a1,a2,a3,a4,a5)=(0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429)
     L = abs(X)
     K=1.0/(1.0+0.2316419*L)
     w=1.0-1.0/sqrt(2*pi)*exp(-L*L/2.)*(a1*K+a2*K*K+a3*pow(K,3)+a4*pow(K,4)+a5*pow(K,5))
     if X<0:
        w=1.0-w
     return w
    
#get user inputs and plug into the formulas
Csp=float(input("Please enter the CALL option current stock price: "))
Cep=float(input("Exercise Price: "))
Ctime=float(input("Maturity (yrs): "))
Crate=float(input("Rate (10% is 0.1): "))
Cstddev=float(input("stddev: "))
print("CALL price is: ", bs_call(Csp,Cep,Ctime,Crate,Cstddev))

Psp=float(input("Please enter the PUT option current stock price: "))
Pep=float(input("Exercise Price: "))
Ptime=float(input("Maturity (yrs): "))
Prate=float(input("Rate (10% is 0.1): "))
Pstddev=float(input("stddev: "))
print("PUT price is: ", bs_put(Psp,Pep,Ptime,Prate,Pstddev))
