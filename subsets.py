#subset extractor algorithm 
#By : Mahmoud Aly
#engma7moud3ly@gmail.com 

#input set
set1={1,2,3,4} 
t1=tuple(set1) 
#output list contain sub-sets
output=[] 

#number of  elements in set1
n=len(set1) 
#predicted number of sub-sets 2^n-1
m=2**n

#extract sub-sets
for i in range(m):
      s=set() 
      for j in range(n):
             b=(i>>j)&1
             if(b==1):s.add(t1[j])
      if(s!=set()):output.append(s)

#sort list of sub-sets by length
output.sort(key=len)

print("input set :",set1)
print("number of sub-sets :",len(output)) 
for s in output:print(s) 

