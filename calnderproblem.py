import datetime  
from datetime import date 
import calendar 
  
def findDay(date): 
    day, month, year = (int(i) for i in date.split('-'))     
    born = datetime.date(day, month, year) 
    return born.strftime("%A") 
  
# Driver program 

test_dict = {"2020-01-01" : 4,
             "2020-01-02" : 4,
             "2020-01-03" : 6,
             "2020-01-04":  8,
             "2020-01-05":  2,
             "2020-01-06":  -6,
             "2020-01-07":  2,
             "2020-01-08":  -2
             }


k =[]
v =[]
week =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
a = []
for i in test_dict :
    key =test_dict[i]  # key
    k.append(key)
    value = findDay(i) # value
    v.append(value)
    l = len(test_dict.values())

# value --> DAYS
# key --> INT
dict ={} #o/p Dict

for i in range(7):
    s=0
    for j in range(len(k)):
        if(week[i] == v[j]):
            s=s+k[j]
    a.append(s)
    dict[week[i]] = a[i]
    
    
print(dict)    #op
    
   
    


    
