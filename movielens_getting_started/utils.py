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


def get_rich_dataset(df_interaction, df_item):
    '''
    영화 타이틀, 장르 및 가독성 있는 날짜를 입력하여 제공
    '''
    df_r = df_interaction.copy()
    df_r.drop(['EVENT_TYPE'], axis=1, inplace=True)
    df_r.drop(['EVENT_VALUE'], axis=1, inplace=True)    

    # Add readable date
    data_col_val = df_r.TIMESTAMP.apply(lambda x: get_readable_date(int(x)))
    df_r.insert(len(df_r.columns),column="DATE", value=data_col_val)    
    # Add item_title, genre using join opeation
    df_r = df_r.merge(df_item, on='ITEM_ID', how='inner')
    col_order = ['USER_ID', 'ITEM_ID','TITLE', 'GENRE', 'TIMESTAMP', 'DATE']
    df_r = df_r[col_order]
    return df_r



