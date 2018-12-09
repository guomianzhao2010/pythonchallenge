import os
import csv
path = os.path.join('election_data.csv')
x=0
can=[]
dup=[]
khan=0
correy=0
li=0
o=0


with open (path) as (csvfile):
    election=csv.reader(csvfile, delimiter=',')   
    for row in election:
        x=x+1
        can.append(row[2])
    vote=x-1
    print ("Total votes: "+ str(vote))
    
    for a in range(0,vote+1):
        if can[a]=="Khan":
            khan=khan+1
        if can[a]=="Correy":
            correy=correy+1
        if can[a]=="Li":
            li=li+1
        if can[a]=="O'Tooley":
             o=o+1
    
    def percentage(part, whole):
        return 100 * float(part)/float(whole)
    
    print ("Khan: "+str(percentage(khan, vote))+"% "+ str(khan))
    print ("Correy: "+ str(percentage(correy, vote))+"% "+str(correy))
    print ("Li: "+str(percentage(li, vote))+"% "+str(li))
    print ("O'Tooley: "+ str(percentage(o, vote))+"% "+str(o))

    winner=[khan, correy, li, o]
    print ("Winner: Khan")
    


   
    
    

