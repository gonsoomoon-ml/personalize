import datetime
import pandas as pd


#####################################
# 데이터 전처리 함수
#####################################

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


#####################################
# 추론 함수 관련
#####################################


def get_item_details(items_df, item_id):
    '''
    해당 ITEM_ID 의 부가 정보를 제공
    예시: get_item_details(items_df, item_id='7bc976b5-c78c-42aa-a4b2-dd734ce1047f')
    '''
    return items_df[items_df['ITEM_ID'] == item_id]

def get_item_list_details(items_df, item_id_list):
    '''
    해당 ITEM_ID 의 부가 정보를 제공
    예시: get_item_details(items_df, item_id='7bc976b5-c78c-42aa-a4b2-dd734ce1047f')
    '''
#    df = pd.DataFrame(columns='ITEM_ID', data=item_id_list)
    df = pd.DataFrame(data={'ITEM_ID':item_id_list})
    rec_item_df = df.merge(items_df)
    return rec_item_df





