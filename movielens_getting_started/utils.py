import datetime

def get_readable_date(unix_timestamp):
    '''
    Return readable date format from unix format
    '''
    return datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_user_groups(df_group, user_id_list):
    '''
    Call example:
user_id_list = [98,160,20, 100]    
    df_user_group = get_user_groups(df, user_id_list)
    df_user_group
    '''
    df_t = df_group.query('USER_ID in @user_id_list' )
    return df_t


