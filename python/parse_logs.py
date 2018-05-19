import os

from fnmatch import fnmatch
import re
import csv

batch = '/home/owl/downloaded_results/batch_correct_1'
exact_set = 'fpr_eop'

path = batch

dirpattern = "*fpr_eop*"
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
       


    #datasets.extend(re.findall("DATASET:", filetext))
    #string = (re.search('REWARDS:\d+', filetext))
    #print string.group(0) 
    #rewards.extend(string.group(0))
    #string = (re.search(('DATASET:\^'), filetext))
    #rewards.extend((re.search('\d+', string)))
    #print string


#print rewards 
        
        
        #if 'REWARD' in inf.read():
         #   print ("tru")
#def open_files(filenames):
 #   for name in filenames:
        #yield open(name, 'r', encoding='utf-8')
        #if 'REWARD' in open(name).read():
  #      print name 
        #print("true")

#def find_files(pattern, top_level_dir):
 #   for path, dirlist, filelist in os.walk('/user/home/owl/downloaded_results/batch_correct_1/chao_4_batch_fpr_eop_batch1/rslt_chao_4_drones_04_nrad_0_nres_4_drad_0_dres_4_b_55_btch_fpr_eop_batch1'):
  #      for name in fnmatch.filter(filelist, pattern):
   #         yield os.path.join(path, name)


#txtfiles = find_files('*.txt')



#def lines_from_files(files):
 #   for f in files:
  #      for line in f:
   #         yield line


#def find_errors(lines):
 #   pattern = re.compile('RESULT:')
  #  for line in lines:
   #     if pattern.search(line):
    #        print(line) 


#m = re.search('RESULT:(d+)', ) 
#m.group(1)

#def find_errors(lines):
 #   pattern = re.compile('RESULT:`')
  #  for line in lines:
    #    if pattern.search(line):
     #         print(line) 


