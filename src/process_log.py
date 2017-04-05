import pandas as pd
from datetime import datetime
import time
import re # regular expression operation

from Feature_1 import feature_1
from Feature_2 import feature_2
from Feature_3 import feature_3
from Feature_4 import feature_4


####### Data load, Preprocess, Store the data in a dataframe #####

#Defined emptly list for each of the features
host_1=[]
timestamp_1=[]
request_1=[]
reply_code_1=[]
bytes_1=[]
Unix_time_1 = []
request_clean = []

#import the contects of log.txt file and process it
with open("log_2.txt", "r") as f:
    for line in f:
        words1 = re.split(" - - \[| -0400\] | ",line)
        host_1.append(words1[0].strip())       # first split part is the host and stored in the host_1 list

        timestamp_1.append(words1[1].strip())
        #convert the time into Unix time
        d = datetime.strptime(words1[1].strip(), "%d/%b/%Y:%H:%M:%S")
        Unix_time_1.append(time.mktime(d.timetuple()))

        n1 = len(words1)
        if (n1==7):
            request = words1[2].strip() + " " + words1[3].strip() + " " + words1[4].strip()
        else:
            request = words1[2].strip() + " " + words1[3].strip()

        request_1.append(request) # the actual request address
        request_clean.append(words1[3].replace("\"","")) #saved in another variable name request_clean
        reply_code_1.append(int(words1[(n1-2)].strip())) # the last part is the reply code]

        bytes = words1[(n1-1)].strip()
        # some of the bytes are listed as '-' which will be replaced with o
        if (bytes.isdigit()): bytes_1.append(int(bytes))
        else: bytes_1.append(0)

#All the data has been stored into a dataframe named df for further analysis
df=pd.DataFrame({"host":host_1, "timestamp":timestamp_1, "request":request_1, "reply_code":reply_code_1, "bytes":bytes_1, "Unix_time":Unix_time_1,"Request_clean":request_clean}) #dataframe to analysis


if (len(df)>0):
    ##feature 1 is processed in Feature_1.py file
    feature_1(df)

    ##feature 2 is processed in Feature_2.py file
    feature_2(df)

    ##feature 3 is processed in Feature_3.py file
    feature_3(df)

    ##feature 4 is processed in Feature_4.py file
    feature_4(df)
