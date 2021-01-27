#用於香水百合價量預測比賽之資料預處理，填補空值。
import pandas as pd
import os
from tqdm import tqdm
import numpy as np
import datetime

#填補空缺日期
# def fill_df(df, lost_list, sum_price_high, sum_price_mid, sum_price_avg, sum_volume):
#     id = len(df) - 1    #原始資料最後一列為'小計'，實際長度為len(df) - 1
#     #取個欄平均
#     avg_price_high = int(sum_price_high / id)
#     avg_price_mid = int(sum_price_mid / id)
#     ang_price_avg = round((sum_price_avg / id), 2)  # 四捨五入制小數點後2位
#     avg_sum_volume = int(sum_volume / id)

#     for add_data in lost_list:  #在dataframe最後面補齊缺失的日期
#         df.loc[id] = [add_data, avg_price_high, avg_price_mid, ang_price_avg, avg_sum_volume]
#         id += 1
#     df = df.sort_values(by=['日　　期'])    #再對日期欄做排序

    return df

def fill_df2(new_df, next_date):    #取前10天的資料平均，填入陣列
    if len(new_df) >= 5:
        arr = new_df[-10:]
        average = np.mean(arr, axis=0)
        new_df.append(average)

    else:
        arr = new_df
        average = np.mean(arr, axis=0)
        new_df.append(average) #填補完之後再把今天的資料加入新陣列
    return new_df



org_fold = r'D:\dataset\lilium_price\org\108-110' #原始資料
fold = r'D:\dataset\lilium_price\preprocessing' #生成資料
start = datetime.datetime(2019, 1,2)   #設定開始日期
end = datetime.datetime(2021, 1, 27)   #設定開始日期

# 建立日期index
idx = []
for i in range((end - start).days + 1):
    idx.append(start + datetime.timedelta(days = i))

csv_list = os.listdir(org_fold)
for file_name in csv_list:
    org_path = os.path.join(org_fold, file_name)
    df = pd.read_excel(org_path, header=4)
    i = 0
    next_date = start

    lost_list = []
    new_df = []
    # sum_price_high, sum_price_mid, sum_price_avg, sum_volume =0, 0, 0, 0
    with tqdm(total=len(df)) as pbar:
        df = df[:-1].drop(['市　　場', '產　　品', '增減%', '增減%.1', '殘貨量', 'Unnamed: 12'], axis=1) #先刪除最後一列(小計)，再刪除特定欄位
        total_day = 0
        for index, row in df.iterrows():
            data_row = df.loc[index].values
            date = data_row[0]   #日期、最高價、上價、中價、下價、平均價、交易量        
            # 轉換日期格式
            year, month, day = int(date.split('/')[0]) + 1911, int(date.split('/')[1]), int(date.split('/')[2])
            date = datetime.datetime(year, month, day)
            # 判斷是否缺值
            if date != next_date:
                interval = (date - next_date).days  # 計算丟失天數
                for i in range(interval):
                    # print('\nmissed:{}, index={}'.format(next_date, index))
                    fill_df2(new_df, next_date)
                    next_date = datetime.timedelta(days = 1)
                new_df.append(data_row[1:]) #填補完之後再把今天的資料加入新陣列
                # 計算前10天的平均值作為填補資料
                # if len(new_df) >= 10:   
            else:
                new_df.append(data_row[1:])

            
            # df.loc[index, '日　　期'] = pd.to_datetime('%d/%d/%d'%(date.year, date.month, date.day))
            # # interval = (date - predate).days
            next_date = date + datetime.timedelta(days = 1)

            # if not interval == 1: #前後兩個日期不相臨
            #     for i in range(interval-1):    #找出中間所有缺少的日期
            #         lost_date = predate + datetime.timedelta(days = (i + 1))
            #         # lost_list.append([lost_date, (prehp+price_high)/2, (premp+price_mid)/2, (preavg+price_avg)/2, (pre_vol+volume)/2])
            #         lost_list.append(lost_date)
            # predate  = date
            # prehp = price_high
            # premp = price_mid
            # preavg = price_avg
            # pre_vol = volume
            


            # 更新進度條
            pbar.update(1)
            pbar.set_description(file_name)
        new_df = pd.DataFrame(new_df)
    
    # df = fill_df(df, lost_list, sum_price_high, sum_price_mid, sum_price_avg, sum_volume)
    new_df.insert(0, '日期', idx)
    new_df.to_csv(os.path.join(fold, file_name[:-4]+'.csv'), encoding='utf_8_sig', index=None,header = ['日期', '最高價', '上價', '中價', '下價', '平均價', '交易量'])