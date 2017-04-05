import time
import pandas as pd

def feature_3(df):
    Start_time_Unix=[] # Initialize a matrix to store the start of each interval
    Count_1=[] # Initialize a matrix to store the visit frequency of each interval
    time_unique = df.Unix_time.unique() # Find the unique time in which there is a website hit

    # As the frequency of website hit changes as a new hit comes
    # A for loop is run at all those unique time to find the total number of website visit at subsequent 1 hour
    for i in time_unique:
        count=df.Unix_time[((df.Unix_time>=i) & (df.Unix_time<(i+3600)))].count() # total website visit is counted
        Start_time_Unix.append(i) # stored the started time
        Count_1.append(count) # stored the count

    Hours=pd.DataFrame({"start_time":Start_time_Unix,"count":Count_1}) # taken into a dataframe
    Hours_sorted = Hours.sort_values(by=["count"],ascending = False) # sorted by no of count
    #Hours_sorted=Hours_sorted.drop_duplicates('count') # duplicated entries are removed
    Hours_10 = Hours_sorted[0:10] # only first 10 data points are considered


    file = open("hours.txt","w") # open a file to write the busiest hours
    for i,r in Hours_10.iterrows():
        file.writelines("%s -0400,%s\n" % (time.strftime("%d/%b/%Y:%H:%M:%S", time.localtime(r["start_time"])),int(r["count"])))
        #file.writelines(" -0400,%s\n" %r["count"])
    file.close()
