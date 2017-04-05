# fancite-analytics-challenge
#### By Shahadat Iqbal

## Language
The program is written in Python language. The vertion that has been used is Python version 2.7.5.

## Pre-built packages, modules, or libraries used
1. Pandas
2. Datetime
3. Time
4. Re (Regular Expression)

## Code details
The main code is written in process_log.py file. For simplicity of the code, this file calls other four files for different Feature analysis.
So there are total five python code files in src folder:
1. process_log.py
2. Feature_1.py
3. Feature_2.py
4. Feature_3.py
5. Feature_4.py

### process_log.py
This file mainly load the raw data, pre-process it, and finally save it into a dataframe. It is easier to do further analysis if the data is converted into a dataframe.  
This code call other function (saved in other files) to extract the Features.

### Feature_1.py
This file contains the code to list the top 10 most active hosts/IP addresses that have accessed the site. 
The code has following steps:
1. Group the data by host
2. Count the number of data points at each group
3. sort the count data
4. Write the top 10 list

### Feature_2.py
This file contains the 10 resources that consume the most bandwidth on the site. 
The code has following steps:
1. Group the data by Request
2. Sum the total bytes (sum) used by each group and also calcualte the total no of datapoints (count) at each group
3. sort the count data by sum and then count
4. Write the top 10 list

### Feature_3.py
This file contains the list of top 10 busiest (or most frequently visited) 60-minute periods. 
The code has following steps:
1. Find a list (time_unique) of times when there is a website visit
2. It is assumed that the total frequency of website hit will change when there is a new visit. So for each item of time_unique list the total number of website visit is calculated for the subsequent one hour
3. Save the start time of the interval and the visit count into a dataframe 
4. Sort the dataframe in decending order according to the number of count 
5. Write the top 10 list

### Feature_4.py
This file contains code to detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes and could be logged in blocked.txt file.
The code has following steps:
1. The data is grouped by host
2. A for loop is run to do the analysis by each group (host)
3. Another for loop is run over the website visit of the host
4. Some conditional clause is writeen to find the prefered security breaches

## Testing
The code has been tested with the provided testing data. Along with a setup dataset has been taken in "you-own-test" folder for further testing. 
