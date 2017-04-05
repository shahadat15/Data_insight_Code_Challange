def feature_1(df):
    df_group= df["host"].groupby(df["host"]).count() # group the data by host name and find the no of entries per host
    df_sort=df_group.sort_values(ascending = False) # sort the data in decending order
    hosts_10=df_sort[0:10,] #take the first 10 lines
    hosts_10.to_csv('hosts.txt',sep=',') # write the file