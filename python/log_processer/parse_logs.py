import os
from operator import itemgetter
from fnmatch import fnmatch
import re
import csv

home_directory = (os.environ['HOME'])

# This script looks for .log files recursively in specified directory.
# Then, it recovers requested data from the .log file as specified.
# It exports the data into a CSV file and sorts it by requested column.


# PARAMS

batch = home_directory + '/downloaded_results/batch_correct_1' # where to look for files
exact_set = 'fpr_res4'                                          # identifier of test (e.g. run1, test2..)
csv_output_folder = home_directory + '/mc_data/csv/'           # where to output csv files 

requested_data = ['PROBLEM_NAME',
                  'BUDGET',
                  'CTIME',
                  'SESSION_TIME',
                  'REWARDS',
                  'MODE']

# CODE

dirpattern = '*' + exact_set + '*' 
logfile_pattern = "*.log"

dirs = []
directories = []

print ("processing logfiles from folders:\n")

path = batch

for root, subdirs, files in os.walk(path):
    for dirname in subdirs:
        if fnmatch(dirname, dirpattern):
            directories.append(dirname)
            print dirname 
    break

print("------------")



for dirpattern in directories:  
    for root, subdirs, files in os.walk(path + '/' + dirpattern):

        dirs.extend(os.path.join(root, name) for name in subdirs)

filenames = []

for directory in dirs:
    for path, subdirs, files in os.walk(directory):
        filenames.extend(os.path.join(path, name) for name in files) 
       

rewards = []
datasets = []  
rw_pattern = "REWARDS:\d+"

print "In total, there are " + str(len(filenames))+ " logfiles in " + str(len(directories)) + " folders."
print str(len(dirs)) + " tests were run, producing " + str(len(filenames)) + " logfiles."  

csv_file_name = csv_output_folder + exact_set + '.csv'

with open(csv_file_name, 'w+') as csvfile:
    fieldnames = requested_data
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for name in filenames:
        #open and load contents to a string
        logfile = open(name, 'r')
        log_insides = logfile.read()
        logfile.close()
      
        #parse items separated by ;
        log_insides = log_insides.split(";")
        csv_entry = [] 
        
        for specific_tag in requested_data: 
            for datatag in log_insides:
                id = datatag.split(":")[0]
                if id == specific_tag:
# We want to parse the data specified by tag
                    raw_value = datatag.split(":")[1]                   
# This removes everything until a forward slash is matched.
# It also keeps the data if no / is present
                    raw_value = re.sub(r".*/", '', raw_value)

# I could do it with regex too, but I want to keep it here in case I need it some day
                    value = raw_value.replace('.txt', '')

                    csv_entry.append(value)
                    
        
   
        csv_row = dict(zip(requested_data, csv_entry))
        writer.writerow(csv_row)


#this should sort based on datasets
with open(csv_file_name, 'r') as f:
    data = [line for line in csv.reader(f)]
    newRecord = requested_data  
    data.sort(key=itemgetter(0))  # 0 is the datasets column

    with open(csv_file_name, 'w') as f:
        csv.writer(f).writerows(data)
