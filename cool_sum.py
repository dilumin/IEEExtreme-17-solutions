import math
#  create a dictionary
def binomial_coefficient(n,i):
  
 if (i==0 or i==n):
    value=1
 elif (i in my  ):
   
    value=my[i] 
 elif (n-i in my):
     value=my[n-i] 
 else:
  value=math.factorial(n)//(math.factorial(i)*math.factorial(n-i))   
  my[i]=value

 return value  



def calculate_a_t(k, n):
    value=2**k
    for t in range (0,value):
      x=0
      i=value*x +t 
      value2=0
      while (n >= i ):
          
          
          value2+=binomial_coefficient(n,i)
          x+=1
          i=value*x +t

      print(value2%998244353)


#  create a dictionary
my={}

k,n=map(int,input().split())
calculate_a_t(k,n)

         