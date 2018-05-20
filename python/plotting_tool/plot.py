import csv
import os
import numpy as np
import matplotlib.pyplot as plt

home_directory = (os.environ['HOME'])


# PARAMS

# where is the CSV file located
path = home_directory + '/mc_data/csv/'

# which CSV to parse and plot
csv_to_print = 'fpr_dtop.csv'

# insert headers which to parse from CSV
what_we_want = ['SESSION_TIME', 'REWARDS']

# alternatively, specify columns to plot
# (note that the headers above have priority)

x_column = 0
y_column = 1

### GRID SETTINGS ###
# if auto_grid is on,
# plot is automatically scaled
auto_grid = True

# range of graph 
x_range = 15
y_range = 800

# spacing between major grid lines
x_grid_spacing = 3
y_grid_spacing = 100 

# specify the first value on the axis
x_start = 0
y_start = 0

# how many minor grid lines for each major
minors_to_major = 5

# whether or not should we plot from the minimal x value
# basically if the graph looks weird, try changing it
sort_x = True

# size of graph
# w = width, h = height

w = 400 
h = 400
monitor_dpi = 96

# CODE
x = []
y = []



found_x = False
found_y = False

csv_path = path + csv_to_print 
with open(csv_path) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rownum, row in enumerate(csvReader):
        if (rownum == 0):
            for column, header in enumerate(row):
                if (header == what_we_want[0]): 
                    x_column = column
                    found_x = True
               
                if (header == what_we_want[1]):
                    y_column = column
                    found_y = True
            if not found_y:
                 print 'tag ' + what_we_want[1] + ' for y not found in header!'     
                 print 'using default - y = column 1'
            if not found_x:
                 print 'tag ' + what_we_want[0] + ' for x not found in header!' 
                 print 'using default - x = column 0'
        
       
        if (rownum > 1):
            x.append(row[x_column])
            y.append(row[y_column])

#plt.figure(figsize=(w/monitor_dpi, h/monitor_dpi), dpi=monitor_dpi)
fig, ax = plt.subplots(figsize=(w/monitor_dpi, h/monitor_dpi), dpi=monitor_dpi)

x = map(float, x)
y = map(float, y)


to_sort = zip(x,y)
to_sort.sort()

result = ([ a for a,b in to_sort ], [ b for a,b in to_sort ])

x = result[0]
y = result[1]

plt.plot(x,y)

#TITLE AND LEGEND
plt.suptitle(csv_to_print, fontsize = 24)
ax.set_xlabel(what_we_want[0], fontsize = 18)
ax.set_ylabel(what_we_want[1], fontsize = 18)

# GRID SETTINGS
#major_ticks = np.arange(0, 150, 10)
#minor_ticks = np.arange(0, 150, 5)

if auto_grid:
    x_range = max(x) 
    x_start = min(x) 
    y_range = max(y)
    y_start = min(y)
    

    x_grid_spacing = (float(x_range - x_start) / float(10))
    y_grid_spacing = (float(y_range - y_start) / float(10))
    minors_to_major=5
    
    y_range += y_grid_spacing


ax.set_ylim(y_start, y_range)
ax.set_xlim(x_start, x_range)

#ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
#ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
# Set major ticks for x axis
major_xticks = np.arange(x_start, x_range, x_grid_spacing)
ax.set_xticks(major_xticks)

# Set major ticks for y axis
major_yticks = np.arange(y_start, y_range, y_grid_spacing)
ax.set_yticks(major_yticks)

# I want minor ticks for x axis
minor_x_spacing = (float(x_grid_spacing)/float(minors_to_major))

minor_xticks = np.arange(x_start, x_range, minor_x_spacing)
ax.set_xticks(minor_xticks, minor=True)

# I want minor ticks for y axis
minor_y_spacing = (float(y_grid_spacing)/float(minors_to_major))

minor_yticks = np.arange(y_start, y_range, minor_y_spacing)
ax.set_yticks(minor_yticks, minor=True)


#print val1
#plt.grid(True)
ax.grid(b=True, which='both')

gridlines = ax.get_xgridlines() + ax.get_ygridlines()
for line in gridlines:
    line.set_linestyle('--')


plt.savefig(csv_to_print + '.svg')
plt.show()








