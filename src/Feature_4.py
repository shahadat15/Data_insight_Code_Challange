def feature_4(df):
    df_group= df.groupby(df.host) # the data is grouped by the host
    file = open("blocked.txt","w") # open a file to write the output

    # A for loop to analysis by each group(i.e. each host)
    for name, group in df_group:
        time_hit_last= 0 # The time when login failed started
        no_of_hit = 0 # no of failed login attempts
        block_flag = 0 # whether the site is blocked for next five minutes or not ( 0 not blocked, 1 blocked)

        # for loop to check each row
        for i,r in group.iterrows():
            if (block_flag==0): # if there is no block
                if ((r["reply_code"] == 401)&(no_of_hit==0)): # If it is the first time failed login attempt
                    time_hit_last = r["Unix_time"] # save the time when the host made the first failed login attempt
                    no_of_hit = 1  # the no of failed login is increased to one
                elif ((r["reply_code"] == 401)&(no_of_hit==1)&((r["Unix_time"]-time_hit_last)<20)): # If it is the second login attempt within 20 seconds
                    no_of_hit = 2 # the no of failed login is increased to two
                elif ((r["reply_code"] == 401)&(no_of_hit==2)&((r["Unix_time"]-time_hit_last)<20)): # If it is the third login attempt within 20 seconds
                    block_flag = 1 # Block flag is on
                    time_hit_last = r["Unix_time"] # time_hit_last is set to the time when the block is started
                    no_of_hit = 0  # the no of failed login is set to zero
                elif ((r["reply_code"] == 401)&((r["Unix_time"]-time_hit_last)>20)): # If second/third login failed attempt is done but not within 20 seconds
                    no_of_hit = 1 # the no of failed login is set to one again
                    time_hit_last = r["Unix_time"] # time_hit_last is set to time as the first failed login attempt
                else:
                    no_of_hit = 0 # Else it is a normal visit and do nothing
            else: # when the block flag is on
                if ((r["Unix_time"]-time_hit_last)<300): # check wheather the new visit is within the 5 minute (300 seconds) block period
                    # write the line in the output file
                    file.writelines("%s - - [%s -0400] %s %s %s\n" % (r["host"],r["timestamp"],r["request"],r["reply_code"],r["bytes"]))
                elif (r["reply_code"] == 401): # If the visit is not within the block period and another login failed attempt
                    block_flag=0 # set the block_flag to no block condition (0)
                    time_hit_last = r["Unix_time"] # Again set the time_hit_last to to time as the first failed login attempt
                    no_of_hit = 1 # the no of failed login is set to one again
                else: # in other case: visit after the block period is over and success of login/visit
                    block_flag=0  # set the block_flag to no block condition (0)
                    no_of_hit = 0 # set to zero
                    time_hit_last = 0 #set to zero
    file.close()
