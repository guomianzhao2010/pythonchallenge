import os
import csv

path = os.path.join('budget_data.csv')
x=0
amount=[]
total=0
change=[]
changes=0
average=0
months=[]

with open (path) as (csvfile):
    budget=csv.reader(csvfile, delimiter=',')
   

    for row in budget:
        x=x+1
        amount.append(row[1])
    amount.pop(0)
    month=x-1
    print ("Total month: "+ str(month))
    

for a in range(0,86):
    total+=int(amount[a])
print ("Total profit: " + str(total) )  

for a in range(0,85):
    change.append(int(amount[a+1])-int(amount[a]))

for num in change:
    changes+=int(num)
average=changes/len(change)
print ( "Average Change:" + str(average))

with open (path) as (csvfile):
    budget=csv.reader(csvfile, delimiter=',')
    for row in budget:
        months.append(row[0])
    
    print ("Greatest Increase in Profits: "+ months[change.index(max(change))+2]+ "($"+ str(max(change)) +")")
    print ("Greatest Decrease in Profits: "+ months[change.index(min(change))+2]+ "($"+ str(min(change)) +")")



