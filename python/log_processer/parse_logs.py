import os

from fnmatch import fnmatch
import re
import csv

home_directory = (os.environ['HOME'])



batch = home_directory + '/downloaded_results/batch_correct_1'
exact_set = 'fpr_eop'
path = batch
csv_output_folder = home_directory + '/mc_data/csv/' 
csv_file_name = csv_output_folder + exact_set + '.csv'


dirpattern = '*' + exact_set + '*' 
logfile_pattern = "*.log"

dirs = []
directories = []

print ("processing logfiles from folders:\n")

for path, subdirs, files in os.walk(path):
    for dirname in subdirs:
        if fnmatch(dirname, dirpattern):
            directories.append(dirname)
            print dirname
    break

print("------------")

for dirpattern in directories:
    
    for path, subdirs, files in os.walk(path + '/' + dirpattern):
        for dirname in subdirs:
            #if fnmatch(dirname, dirpattern):
           #print dirname
               dirs.extend(os.path.join(path, name) for name in subdirs)
           

           # dirs.extend(os.path.join(path, dirname))
           # for name in files:
            #     if fnmatch(name, pattern):
                   # f.extend(name)
             #       print os.path.join(path, name)
#print dirs

filenames = []

for directory in dirs:
    for path, subdirs, files in os.walk(directory):
        filenames.extend(os.path.join(path, name) for name in files) 
       
requested_data = ['CTIME',
                  'PROBLEM_NAME',
                  'SESSION_TIME',
                  'REWARDS']

rewards = []
datasets = []  
rw_pattern = "REWARDS:\d+"

for name in filenames:
    #open and load contents to a string
    logfile = open(name, 'r')
    log_insides = logfile.read()
    logfile.close()
  
    #parse items separated by ;
    log_insides = log_insides.split(";")
    #print log_insides
    for specific_tag in requested_data: 
        for datatag in log_insides:
            if datatag.split(":")[0] == specific_tag:
                #print tag.split(":")[1]
                rewards.append(datatag.split(":")[1])
       

with open(csv_file_name, 'a+') as csvfile:
    fieldnames = ['dataset', 'rewards', 'ctime', 'sessiontime']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'dataset': 'Baked', 'rewards': 'Beans'})
