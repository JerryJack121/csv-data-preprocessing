#用於香水百合價量預測比賽之資料預處理，填補空值。
import pandas as pd
import os
from tqdm import tqdm
import numpy as np
import datetime

#填補空缺日期
def fill_df(df, lost_list, sum_price_high, sum_price_mid, sum_price_avg, sum_volume):
    id = len(df)
    #取個欄平均
    avg_price_high = int(sum_price_high / id)
    avg_price_mid = int(sum_price_mid / id)
    ang_price_avg = round((sum_price_avg / id), 2)  # 四捨五入制小數點後2位
    avg_sum_volume = int(sum_volume / id)

    for add_data in lost_list:  #在dataframe最後面補齊缺失的日期
        df.loc[id] = [add_data, avg_price_high, avg_price_mid, ang_price_avg, avg_sum_volume]
        id += 1
    df = df.sort_values(by=['日　　期'])    #再對日期欄做排序

    return df

org_fold = r'D:\dataset\lilium_price\org' #原始資料
fold = r'D:\dataset\lilium_price\generate_dataset' #生成資料
year = '100-110'
# file_name ='FS859.xls'
org_fold = os.path.join(org_fold, year)
for file_name in os.listdir(org_fold):
    org_path = os.path.join(org_fold, file_name)
    df = pd.read_excel(org_path, header=4)
    i = 0
    # predate, prehp, premp, preavg, pre_vol = datetime.datetime(2010, 12,31), 0, 0, 0, 0 #設定日期在開始日期的前一天
    lost_list = []
    sum_price_high, sum_price_mid, sum_price_avg, sum_volume =0, 0, 0, 0
    with tqdm(total=len(df)-1) as pbar:
        df = df.drop(['市　　場', '產　　品', '最高價', '下價', '增減%', '增減%.1', '殘貨量', 'Unnamed: 12'], axis=1) #刪除特定欄位
        for index, row in df.iterrows():
            data_row = df.loc[index].values
            date, price_high, price_mid, price_avg, volume= data_row    #日期、上價、中價、平均價、交易量        
            if date == '小　　計':
                break
            sum_price_high += price_high
            sum_price_mid += price_mid
            sum_price_avg +=price_avg
            sum_volume += volume
            year = int(date.split('/')[0]) + 1911
            month = int(date.split('/')[1])
            day = int(date.split('/')[2])
            date = datetime.datetime(year, month, day)
            df.loc[index, '日　　期'] = pd.to_datetime('%d/%d/%d'%(date.year, date.month, date.day))
            # interval = (date - predate).days
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

    # df = fill_df(df[0:-1], lost_list, sum_price_high, sum_price_mid, sum_price_avg, sum_volume)
    df[0:-1].to_csv(os.path.join(fold, file_name[:-4]+'.csv'), encoding='utf_8_sig', index=False)   #原始資料最後一列為'小計'