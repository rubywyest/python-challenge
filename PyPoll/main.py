import os
import csv

import itertools

election_data = os.path.join("C:/Users/ruby/Google Drive/CloneGitlab/RU-HOU-DATA-PT-09-2019-U-C/Homework/03-Python/Instructions/PyPoll","Resources","election_data.csv")


candidates = {}


with open(election_data,'r')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    
    for row in csvreader:
#        voterid = row[0]
#        county = row[1]
        candidate = row[2]
                         
        if(candidates.get(candidate) is None):
            candidates[candidate] = 1
        else:
            candidates[candidate] = candidates[candidate] + 1
                                 
sum_all_votes = sum(candidates.values())
candi_max = max(candidates.keys(), key=(lambda h:  candidates[h]))

print(f"Election Results")
print(f"____________________")
print(f"Total Voters:{sum_all_votes}")
print(f"__________________________")

for candidate in candidates:
    print(f"{candidate}: {format((candidates[candidate] * 100/ sum_all_votes), '.2f')}% ({candidates[candidate]}) ")
#    print(str(candi['name']))
#    print(len(candi["voters"]))
#    print()
        
#print(allcandis)
print(f"-----------------------")
print(f"Winner: {candi_max}")
print(f"-----------------------")

output_path = os.path.join("C:/Users/ruby/Google Drive/bootcamp/homework/03-Python/python-challenge/", "output", "pybank.txt")

pypollFile = open("C:/Users/ruby/Google Drive/bootcamp/homework/03-Python/python-challenge/output/pyPoll.txt","w") 
pypollFile.write(f"-----------------------" + "\n")
pypollFile.write(f"Election Results" + "\n")
pypollFile.write(f"____________________" + "\n")
pypollFile.write(f"Total Voters:{sum_all_votes}" + "\n")
pypollFile.write(f"__________________________" + "\n")

for candidate in candidates:
    pypollFile.write(f"{candidate}: {format((candidates[candidate] * 100/ sum_all_votes), '.2f')}% ({candidates[candidate]}) " + "\n")
        
#print(allcandis)
pypollFile.write(f"-----------------------" + "\n")
pypollFile.write(f"Winner: {candi_max}" + "\n")
pypollFile.write(f"-----------------------" + "\n")
pypollFile.close() 


