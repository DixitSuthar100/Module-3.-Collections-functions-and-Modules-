'''Write a Python script to print a dictionary where the keys are numbers 
   between 1 and 15.''' 

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)



d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) 
