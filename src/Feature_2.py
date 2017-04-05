def feature_2(df):
    df_group= df.groupby('Request_clean')['bytes'].agg(['sum','count']) # group the data by request and then aggregte the sum and count of bytes
    df_sort=df_group.sort_values(by=['sum','count'],ascending = [False,False]) # sort the data in decending order
    resources_10=df_sort[0:10] #take the first 10 lines
    resources_10.to_csv('resources.txt',sep=',',columns=[],header=False) # write the file

